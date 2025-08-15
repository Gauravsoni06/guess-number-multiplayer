# 🎮 Multiplayer Game Hub

A real-time multiplayer gaming platform featuring multiple games with Socket.IO integration.

## 🎯 **Games Available**

### 1. **Guess the Number** 🎯
- Classic number guessing game (1-100)
- Real-time multiplayer with chat
- Admin controls for round management
- Score tracking and leaderboards

### 2. **Street Food Showdown** 🍽️
- Test your knowledge of Indian street food
- Multiple choice questions with descriptions
- Image hints revealed during gameplay
- Special round types: Normal, Slang, Reverse, Fusion
- 5 rounds per game with comprehensive scoring

## 🚀 **Quick Start**

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd multiplayer-game-hub
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to `http://localhost:5000`
   - Open multiple browser tabs to test multiplayer functionality

## 🎮 **How to Play**

### **Game Selection**
1. Open the game in your browser
2. Choose between "Guess the Number" or "Street Food Showdown"
3. Create a room or join an existing one

### **Room Management**
1. **Create Room**: Enter your nickname and create a new room
2. **Join Room**: Enter your nickname and the 6-digit room code
3. **Share Code**: Share the room code with friends to join

### **Admin Controls**
- The first player to join becomes the admin
- Admin can select game type and start rounds
- If admin leaves, admin role transfers to next player

### **Guess the Number Game**
1. Admin starts a round
2. Server picks a random number (1-100)
3. Players take turns guessing
4. Server responds with "Too High", "Too Low", or "Correct!"
5. First correct guess wins the round
6. Admin can start new rounds

### **Street Food Showdown Game**
1. Admin selects "Street Food Showdown" and starts the game
2. Each round features a different Indian street food
3. **Round Structure:**
   - **Description Phase** (15s): Read the food description
   - **Image Hint** (15s): See the food image
   - **Answer Phase**: Choose from 4 multiple choice options
4. **Scoring:**
   - Base: 10 points for correct answer
   - Speed bonus: +5 points for quick answers
   - Image penalty: -2 points after image reveal
5. **Special Rounds:**
   - **Normal**: Standard description → image flow
   - **Slang**: Include local Hindi names
   - **Reverse**: Image first, then description
   - **Fusion**: Fun made-up fusion foods
6. **Game End**: After 5 rounds, final leaderboard is shown

## 🛠️ **Technical Features**

### **Backend (Python Flask + Socket.IO)**
- Real-time bidirectional communication
- Room-based multiplayer system
- Admin role management
- Game state synchronization
- Chat functionality
- Score tracking

### **Frontend (HTML/CSS/JavaScript)**
- Responsive design for desktop and mobile
- Real-time UI updates
- Game selection interface
- Chat system
- Player list and score display
- Timer and round management

### **Game Features**
- **Modular Architecture**: Easy to add new games
- **Real-time Updates**: Live score updates and chat
- **Admin Controls**: Game management and round control
- **Player Management**: Join/leave handling with admin transfer
- **Error Handling**: Graceful error management
- **Mobile Support**: Responsive design for all devices

## 📱 **Multiplayer Testing**

### **Local Testing**
1. Start the server: `python app.py`
2. Open multiple browser tabs/windows
3. Join the same room with different nicknames
4. Test all game features simultaneously

### **Network Testing**
1. Find your local IP address
2. Share the IP with friends on the same network
3. Friends can access via `http://YOUR_IP:5000`

## 🚀 **Deployment**

### **Quick Deployment Scripts**
- **Windows**: Run `start_app.bat`
- **PowerShell**: Run `start_app.ps1`

### **Manual Deployment**
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`
3. Access via browser at the displayed URL

### **Production Deployment**
The app includes configuration files for various hosting platforms:
- **Railway**: `railway.json`
- **Render**: `render.yaml`
- **Heroku**: `Procfile`
- **Fly.io**: `fly.toml`
- **Vercel**: `vercel.json`

## 🎯 **Game Data**

### **Street Food Dataset**
The game includes 8 authentic Indian street foods:
- Pani Puri (Golgappa, Phuchka)
- Vada Pav (Bombay Burger)
- Samosa
- Dosa
- Bhel Puri
- Pav Bhaji
- Chaat
- Kebab

Each food includes:
- Official name
- Detailed description
- Local slang names
- Search terms for image fetching

## 🔧 **Customization**

### **Adding New Games**
1. Add game logic to `app.py`
2. Update frontend in `templates/index.html`
3. Add game selection options
4. Test thoroughly

### **Adding More Street Foods**
1. Add new entries to the `STREET_FOODS` list in `app.py`
2. Include name, description, slang names, and search terms
3. Test with the game

## 🐛 **Troubleshooting**

### **Common Issues**
1. **Port already in use**: Change port in `app.py` or kill existing process
2. **Dependencies not found**: Ensure virtual environment is activated
3. **Socket connection failed**: Check firewall settings
4. **Game not starting**: Ensure admin has selected a game type

### **Debug Mode**
The app runs in debug mode by default. For production, set `debug=False` in `app.py`.

## 📄 **License**

This project is open source and available under the MIT License.

## 🤝 **Contributing**

Feel free to contribute by:
- Adding new games
- Improving the UI/UX
- Adding more street food items
- Enhancing the scoring system
- Adding new features

## 🎉 **Enjoy Playing!**

The Multiplayer Game Hub is now ready for hours of fun with friends! Test your number guessing skills or challenge your knowledge of Indian street food in this engaging multiplayer experience.

---

**Built with ❤️ using Python Flask, Socket.IO, and modern web technologies** 