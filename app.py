from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory game state with rooms
rooms = {}  # {room_code: {target_number, players, game_active}}

def generate_room_code():
    """Generate a random 6-character room code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/rooms', methods=['POST'])
def create_room():
    """Create a new room"""
    room_code = generate_room_code()
    rooms[room_code] = {
        'target_number': random.randint(1, 100),
        'players': {},
        'game_active': True
    }
    return jsonify({'success': True, 'room_code': room_code})

@app.route('/api/rooms/<room_code>', methods=['GET'])
def get_room(room_code):
    """Get room information"""
    if room_code not in rooms:
        return jsonify({'success': False, 'error': 'Room not found'}), 404
    return jsonify({'success': True, 'room': rooms[room_code]})

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

@socketio.on('join_room')
def handle_join_room(data):
    room_code = data.get('room_code', '').upper()
    nickname = data.get('nickname', 'Anonymous')
    
    if room_code not in rooms:
        emit('error', {'message': 'Room not found!'})
        return
    
    # Add player to room
    rooms[room_code]['players'][request.sid] = {
        'nickname': nickname,
        'score': 0
    }
    
    join_room(room_code)
    emit('joined_room', {
        'room_code': room_code,
        'nickname': nickname,
        'players': list(rooms[room_code]['players'].values())
    }, room=room_code)

@socketio.on('guess')
def handle_guess(data):
    room_code = data.get('room_code', '').upper()
    if room_code not in rooms:
        return
    
    room = rooms[room_code]
    if not room['game_active']:
        return
    
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
        room['game_active'] = False
        
        emit('feedback', {
            'message': f'🎉 {player["nickname"]} guessed correctly! The number was {room["target_number"]}',
            'correct': True
        }, room=room_code)
        
        # Reset game after 3 seconds
        socketio.sleep(3)
        room['target_number'] = random.randint(1, 100)
        room['game_active'] = True
        
        emit('game_reset', {
            'message': f'New round! Guess a number between 1-100',
            'players': list(room['players'].values())
        }, room=room_code)
        
    elif guess < room['target_number']:
        emit('feedback', {'message': 'Too Low! 📉'})
    else:
        emit('feedback', {'message': 'Too High! 📈'})

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
    if room_code in rooms and request.sid in rooms[room_code]['players']:
        # Get player nickname before removing
        player_nickname = rooms[room_code]['players'][request.sid]['nickname']
        
        # Remove player from room
        del rooms[room_code]['players'][request.sid]
        leave_room(room_code)
        
        # Notify other players
        emit('player_left', {
            'players': list(rooms[room_code]['players'].values())
        }, room=room_code)
        
        # Send chat message about player leaving
        emit('chat_message', {
            'nickname': 'System',
            'message': f'{player_nickname} left the room'
        }, room=room_code)
        
        # Delete empty rooms
        if not rooms[room_code]['players']:
            del rooms[room_code]

@socketio.on('disconnect')
def handle_disconnect():
    # Remove player from all rooms
    for room_code, room in rooms.items():
        if request.sid in room['players']:
            # Get player nickname before removing
            player_nickname = room['players'][request.sid]['nickname']
            
            del room['players'][request.sid]
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

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000) 