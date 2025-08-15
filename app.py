from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import random
import string
import time
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Game state storage
rooms = {}

# Street Food dataset
STREET_FOODS = [
    {
        "name": "Pani Puri",
        "description": "A crispy hollow sphere filled with tangy spiced water and potato mix.",
        "slang": ["Golgappa", "Phuchka"],
        "search_terms": "pani puri golgappa indian street food"
    },
    {
        "name": "Vada Pav",
        "description": "A spicy potato fritter served inside a bun with chutneys.",
        "slang": ["Bombay Burger"],
        "search_terms": "vada pav bombay burger indian street food"
    },
    {
        "name": "Samosa",
        "description": "A crispy pastry filled with spiced potatoes and peas.",
        "slang": ["Samosa"],
        "search_terms": "samosa indian street food"
    },
    {
        "name": "Dosa",
        "description": "A thin, crispy crepe made from fermented rice and lentil batter.",
        "slang": ["Dosa"],
        "search_terms": "dosa indian street food"
    },
    {
        "name": "Bhel Puri",
        "description": "A mixture of puffed rice, vegetables, and tangy chutneys.",
        "slang": ["Bhel"],
        "search_terms": "bhel puri indian street food"
    },
    {
        "name": "Pav Bhaji",
        "description": "Spiced mashed vegetables served with buttered bread rolls.",
        "slang": ["Pav Bhaji"],
        "search_terms": "pav bhaji indian street food"
    },
    {
        "name": "Chaat",
        "description": "A savory snack with crispy base, yogurt, and various toppings.",
        "slang": ["Chaat"],
        "search_terms": "chaat indian street food"
    },
    {
        "name": "Kebab",
        "description": "Grilled meat or vegetable skewers with aromatic spices.",
        "slang": ["Kebab"],
        "search_terms": "kebab indian street food"
    }
]

# Image cache for performance
image_cache = {}

def generate_room_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def get_random_food():
    return random.choice(STREET_FOODS)

def get_food_options(correct_food, count=4):
    """Generate multiple choice options including the correct answer"""
    options = [correct_food['name']]
    
    # Add random incorrect options
    other_foods = [food for food in STREET_FOODS if food['name'] != correct_food['name']]
    random.shuffle(other_foods)
    
    for food in other_foods[:count-1]:
        options.append(food['name'])
    
    random.shuffle(options)
    return options

def fetch_food_image(food_name, search_terms):
    """Fetch food image from Unsplash API"""
    if food_name in image_cache:
        return image_cache[food_name]
    
    try:
        # Using Unsplash API (you'll need to sign up for a free API key)
        # For now, using a placeholder approach
        api_url = f"https://api.unsplash.com/search/photos"
        params = {
            'query': search_terms,
            'per_page': 1,
            'orientation': 'landscape'
        }
        headers = {
            'Authorization': 'Client-ID YOUR_UNSPLASH_ACCESS_KEY'  # Replace with actual key
        }
        
        # For demo purposes, using a placeholder image
        # In production, you'd make the actual API call
        placeholder_image = f"https://source.unsplash.com/featured/?{search_terms.replace(' ', '+')}"
        
        image_cache[food_name] = placeholder_image
        return placeholder_image
        
    except Exception as e:
        print(f"Error fetching image: {e}")
        # Fallback to a generic food image
        return "https://source.unsplash.com/featured/?indian+food"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/rooms', methods=['POST'])
def create_room():
    room_code = generate_room_code()
    rooms[room_code] = {
        'players': {},
        'admin_nickname': None,
        'game_type': None,  # 'number_guess' or 'street_food'
        'game_active': False,
        'round_active': False,
        'target_number': None,
        'round_number': 0,
        'max_rounds': 5,
        'current_food': None,
        'food_options': [],
        'round_start_time': None,
        'round_duration': 30,  # 30 seconds per round
        'image_revealed': False,
        'round_type': 'normal'  # 'normal', 'reverse', 'slang', 'fusion'
    }
    return jsonify({'room_code': room_code})

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    # Remove player from all rooms
    for room_code, room in rooms.items():
        if request.sid in room['players']:
            # Get player nickname before removing
            player_nickname = room['players'][request.sid]['nickname']

            # Check if admin is disconnecting
            is_admin = player_nickname == room['admin_nickname']

            del room['players'][request.sid]

            # Transfer admin to next player if admin left
            if is_admin and room['players']:
                new_admin_sid = next(iter(room['players']))
                new_admin_nickname = room['players'][new_admin_sid]['nickname']
                room['admin_nickname'] = new_admin_nickname

                emit('admin_transferred', {
                    'new_admin': new_admin_nickname,
                    'players': list(room['players'].values())
                }, room=room_code)

                emit('chat_message', {
                    'nickname': 'System',
                    'message': f'👑 {new_admin_nickname} is now the admin'
                }, room=room_code)

            emit('player_left', {
                'players': list(room['players'].values())
            }, room=room_code)

            # Send chat message about player disconnecting
            emit('chat_message', {
                'nickname': 'System',
                'message': f'{player_nickname} disconnected'
            }, room=room_code)

            # Delete empty rooms
            if not room['players']:
                del rooms[room_code]
            break
    print(f'Client disconnected: {request.sid}')

@socketio.on('join_room')
def handle_join_room(data):
    room_code = data.get('room_code', '').upper()
    nickname = data.get('nickname', '').strip()
    
    if not nickname or not room_code:
        emit('error', {'message': 'Please provide both room code and nickname!'})
        return
    
    if room_code not in rooms:
        print(f"Room {room_code} not found")  # Debug log
        emit('error', {'message': 'Room not found!'})
        return
    
    print(f"Room found: {room_code}")  # Debug log
    print(f"Current admin_nickname: {rooms[room_code].get('admin_nickname', 'None')}")  # Debug log
    print(f"Current nickname: {nickname}")  # Debug log
    
    # Check if this is the first player BEFORE adding them
    is_first_player = len(rooms[room_code]['players']) == 0
    
    # Add player to room
    rooms[room_code]['players'][request.sid] = {
        'nickname': nickname,
        'score': 0,
        'ready': False
    }
    
    # Set admin if this is the first player
    if is_first_player:
        rooms[room_code]['admin_nickname'] = nickname
        print(f"Set admin_nickname to: {nickname} (first player)")  # Debug log
    
    # Check if this nickname is already admin (for reconnection)
    is_admin = nickname == rooms[room_code]['admin_nickname']
    print(f"Is admin: {is_admin}")  # Debug log
    
    # If no admin exists and this is not the first player, make this player admin
    if not rooms[room_code]['admin_nickname'] and not is_first_player:
        rooms[room_code]['admin_nickname'] = nickname
        is_admin = True
        print(f"Set admin_nickname to: {nickname} (no admin existed)")  # Debug log
    
    # Handle multiple players with same nickname - only first one gets admin
    if nickname == rooms[room_code]['admin_nickname']:
        # Count how many players have this admin nickname
        admin_players = [sid for sid, player in rooms[room_code]['players'].items() 
                        if player['nickname'] == rooms[room_code]['admin_nickname']]
        
        # Only the first player with this nickname should be admin
        if request.sid != admin_players[0]:
            is_admin = False
            print(f"Multiple players with admin nickname '{nickname}' - only first one is admin")
        else:
            print(f"First player with admin nickname '{nickname}' - keeping admin status")
    
    # Debug: Print final admin status
    print(f"Final admin status for {nickname}: {is_admin}")
    
    # Prepare the data to send
    join_data = {
        'room_code': room_code,
        'nickname': nickname,
        'players': list(rooms[room_code]['players'].values()),
        'is_admin': is_admin,
        'round_active': rooms[room_code]['round_active'],
        'game_type': rooms[room_code]['game_type']
    }
    
    print(f"Sending joined_room data: {join_data}")  # Debug log
    
    join_room(room_code)
    # Send joined_room event only to the player who joined
    emit('joined_room', join_data)
    
    # Notify other players about the new player
    emit('player_joined', {
        'nickname': nickname,
        'players': list(rooms[room_code]['players'].values())
    }, room=room_code, include_self=False)

@socketio.on('select_game')
def handle_select_game(data):
    room_code = data.get('room_code', '').upper()
    game_type = data.get('game_type')
    
    if room_code not in rooms:
        return
    
    room = rooms[room_code]
    player = room['players'].get(request.sid)
    
    if not player or player['nickname'] != room['admin_nickname']:
        return
    
    room['game_type'] = game_type
    room['game_active'] = False
    room['round_active'] = False
    
    emit('game_selected', {
        'game_type': game_type,
        'message': f'Game selected: {game_type.replace("_", " ").title()}'
    }, room=room_code)
    
    emit('chat_message', {
        'nickname': 'System',
        'message': f'🎮 {game_type.replace("_", " ").title()} selected! Admin can start the game.'
    }, room=room_code)

@socketio.on('start_round')
def handle_start_round(data):
    print(f"Start round event received: {data}")  # Debug log
    room_code = data.get('room_code', '').upper()
    if room_code not in rooms:
        print(f"Room {room_code} not found")  # Debug log
        return
    
    room = rooms[room_code]
    player = room['players'].get(request.sid)
    
    if not player or player['nickname'] != room['admin_nickname']:
        print(f"Player {player['nickname'] if player else 'None'} is not admin")  # Debug log
        return
    
    if room['game_type'] == 'number_guess':
        # Start number guessing round
        room['target_number'] = random.randint(1, 100)
        room['round_active'] = True
        room['game_active'] = True
        
        emit('round_started', {
            'message': '🎮 Round started! Guess a number between 1-100',
            'players': list(room['players'].values())
        }, room=room_code)
        
        emit('chat_message', {
            'nickname': 'System',
            'message': '🎮 New round started!'
        }, room=room_code)
        
    elif room['game_type'] == 'street_food':
        # Start street food round
        room['round_number'] += 1
        room['round_active'] = True
        room['game_active'] = True
        room['round_start_time'] = time.time()
        room['image_revealed'] = False
        
        # Select random food and round type
        room['current_food'] = get_random_food()
        room['food_options'] = get_food_options(room['current_food'])
        
        # Determine round type (20% chance for special rounds)
        if random.random() < 0.2:
            room['round_type'] = random.choice(['reverse', 'slang', 'fusion'])
        else:
            room['round_type'] = 'normal'
        
        # Prepare round data
        round_data = {
            'round_number': room['round_number'],
            'max_rounds': room['max_rounds'],
            'round_type': room['round_type'],
            'duration': room['round_duration'],
            'players': list(room['players'].values())
        }
        
        if room['round_type'] == 'normal':
            round_data['description'] = room['current_food']['description']
            round_data['options'] = room['food_options']
        elif room['round_type'] == 'slang':
            # Use Hindi/local description
            round_data['description'] = f"Local name: {random.choice(room['current_food']['slang'])} - {room['current_food']['description']}"
            round_data['options'] = room['food_options']
        elif room['round_type'] == 'reverse':
            # Show image first (blurred)
            image_url = fetch_food_image(room['current_food']['name'], room['current_food']['search_terms'])
            round_data['image_url'] = image_url
            round_data['options'] = room['food_options']
        elif room['round_type'] == 'fusion':
            # Made-up fusion food
            fusion_foods = ['Pizza Dosa', 'Burger Samosa', 'Taco Puri', 'Sushi Chaat']
            round_data['description'] = f"Fusion food: {random.choice(fusion_foods)} - {room['current_food']['description']}"
            round_data['options'] = room['food_options']
        
        emit('street_food_round_started', round_data, room=room_code)
        
        emit('chat_message', {
            'nickname': 'System',
            'message': f'🍽️ Street Food Round {room["round_number"]} started!'
        }, room=room_code)
        
        # Schedule image reveal for halfway point
        socketio.sleep(room['round_duration'] // 2)
        if room['round_active'] and room['round_type'] != 'reverse':
            room['image_revealed'] = True
            image_url = fetch_food_image(room['current_food']['name'], room['current_food']['search_terms'])
            emit('image_revealed', {
                'image_url': image_url,
                'message': '🖼️ Here\'s a hint!'
            }, room=room_code)
        
        # Schedule round end
        socketio.sleep(room['round_duration'] // 2)
        if room['round_active']:
            handle_street_food_round_end(room_code)

@socketio.on('guess')
def handle_guess(data):
    room_code = data.get('room_code', '').upper()
    if room_code not in rooms:
        return
    
    room = rooms[room_code]
    if not room['game_active'] or not room['round_active']:
        emit('feedback', {'message': 'Round not started yet! Wait for admin to start.'})
        return
    
    if room['game_type'] == 'number_guess':
        handle_number_guess(data, room, room_code)
    elif room['game_type'] == 'street_food':
        handle_street_food_guess(data, room, room_code)

def handle_number_guess(data, room, room_code):
    guess = data.get('guess')
    try:
        guess = int(guess)
    except:
        emit('feedback', {'message': 'Please enter a valid number!'})
        return
    
    if guess < 1 or guess > 100:
        emit('feedback', {'message': 'Please guess a number between 1-100!'})
        return
    
    player = room['players'].get(request.sid)
    if not player:
        return
    
    if guess == room['target_number']:
        # Correct guess!
        player['score'] += 1
        room['round_active'] = False  # End the round
        
        emit('feedback', {
            'message': f'🎉 {player["nickname"]} guessed correctly! The number was {room["target_number"]}',
            'correct': True
        }, room=room_code)
        
        emit('round_ended', {
            'message': f'Round ended! {player["nickname"]} wins! Admin can start a new round.',
            'players': list(room['players'].values())
        }, room=room_code)
        
        emit('chat_message', {
            'nickname': 'System',
            'message': f'🎉 {player["nickname"]} won the round! Admin can start a new round.'
        }, room=room_code)
        
    elif guess < room['target_number']:
        emit('feedback', {'message': 'Too Low! 📉'})
    else:
        emit('feedback', {'message': 'Too High! 📈'})

def handle_street_food_guess(data, room, room_code):
    answer = data.get('answer')
    player = room['players'].get(request.sid)
    
    if not player or not answer:
        return
    
    # Check if player already answered
    if player.get('answered'):
        emit('feedback', {'message': 'You already answered this round!'})
        return
    
    player['answered'] = True
    player['answer'] = answer
    player['answer_time'] = time.time()
    
    # Check if correct
    is_correct = answer == room['current_food']['name']
    
    if is_correct:
        # Calculate points based on speed and image reveal
        time_taken = player['answer_time'] - room['round_start_time']
        base_points = 10
        
        if time_taken < room['round_duration'] // 2:
            # Answered before image reveal
            speed_bonus = max(0, 5 - int(time_taken))
            points = base_points + speed_bonus
        else:
            # Answered after image reveal
            points = base_points - 2
        
        player['score'] += points
        
        emit('feedback', {
            'message': f'🎉 Correct! +{points} points!',
            'correct': True
        })
    else:
        emit('feedback', {
            'message': f'❌ Wrong! The answer was {room["current_food"]["name"]}',
            'correct': False
        })
    
    # Check if all players answered
    all_answered = all(p.get('answered') for p in room['players'].values())
    if all_answered:
        handle_street_food_round_end(room_code)

def handle_street_food_round_end(room_code):
    room = rooms[room_code]
    room['round_active'] = False
    
    # Show results
    results = []
    for player in room['players'].values():
        results.append({
            'nickname': player['nickname'],
            'answer': player.get('answer', 'No answer'),
            'correct': player.get('answer') == room['current_food']['name'],
            'score': player['score']
        })
    
    emit('street_food_round_ended', {
        'results': results,
        'correct_answer': room['current_food']['name'],
        'round_number': room['round_number'],
        'max_rounds': room['max_rounds'],
        'players': list(room['players'].values())
    }, room=room_code)
    
    # Reset player answers for next round
    for player in room['players'].values():
        player['answered'] = False
        player['answer'] = None
        player['answer_time'] = None
    
    # Check if game is over
    if room['round_number'] >= room['max_rounds']:
        # Game over - show final results
        final_results = sorted(room['players'].values(), key=lambda p: p['score'], reverse=True)
        emit('street_food_game_ended', {
            'final_results': final_results,
            'winner': final_results[0]['nickname'] if final_results else None
        }, room=room_code)
        
        emit('chat_message', {
            'nickname': 'System',
            'message': f'🏆 Game Over! {final_results[0]["nickname"]} wins with {final_results[0]["score"]} points!'
        }, room=room_code)
        
        room['game_active'] = False
        room['round_number'] = 0
    else:
        # Continue to next round
        emit('chat_message', {
            'nickname': 'System',
            'message': f'Round {room["round_number"]} complete! Admin can start round {room["round_number"] + 1}.'
        }, room=room_code)

@socketio.on('chat')
def handle_chat(data):
    room_code = data.get('room_code', '').upper()
    message = data.get('message', '').strip()
    
    if not message or room_code not in rooms:
        return
    
    player = rooms[room_code]['players'].get(request.sid)
    if not player:
        return
    
    emit('chat_message', {
        'nickname': player['nickname'],
        'message': message
    }, room=room_code)

@socketio.on('leave_room')
def handle_leave_room(data):
    room_code = data.get('room_code', '').upper()
    if room_code not in rooms:
        return
    
    room = rooms[room_code]
    if request.sid not in room['players']:
        return
    
    player_nickname = room['players'][request.sid]['nickname']
    is_admin = player_nickname == room['admin_nickname']
    
    del room['players'][request.sid]
    leave_room(room_code)
    
    # Transfer admin if needed
    if is_admin and room['players']:
        new_admin_sid = next(iter(room['players']))
        new_admin_nickname = room['players'][new_admin_sid]['nickname']
        room['admin_nickname'] = new_admin_nickname
        
        emit('admin_transferred', {
            'new_admin': new_admin_nickname,
            'players': list(room['players'].values())
        }, room=room_code)
        
        emit('chat_message', {
            'nickname': 'System',
            'message': f'👑 {new_admin_nickname} is now the admin'
        }, room=room_code)
    
    emit('player_left', {
        'players': list(room['players'].values())
    }, room=room_code)
    
    emit('chat_message', {
        'nickname': 'System',
        'message': f'{player_nickname} left the room'
    }, room=room_code)
    
    # Delete empty rooms
    if not room['players']:
        del rooms[room_code]

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 