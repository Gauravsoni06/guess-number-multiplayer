# 🎯 Guess the Number - Multiplayer Game

A minimal AI-powered multiplayer web game where players compete to guess a random number between 1-100 in real-time with room-based gameplay.

## 🎮 Game Features

- **Room-based multiplayer gameplay** - Create or join game rooms
- **Real-time communication** using Socket.IO
- **Live chat system** for player communication
- **Player score tracking** with persistent scores during rounds
- **Automatic game reset** after each correct guess
- **Responsive design** that works on desktop and mobile
- **No external dependencies** - runs completely locally

## 🛠️ Tech Stack

- **Backend**: Python Flask with Socket.IO
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Database**: In-memory storage (Python dictionary)
- **Real-time Communication**: Socket.IO
- **Deployment**: Heroku, Render, Railway, or any Python hosting platform

## 📋 Requirements

- Python 3.7+
- pip (Python package installer)

## 🚀 Quick Start (Local)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

### 3. Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

## 🎯 How to Play

1. **Welcome Screen**: Choose to create a new room or join an existing one
2. **Create Room**: Enter your nickname and click "Create Room" to get a room code
3. **Join Room**: Enter your nickname and the room code shared by a friend
4. **Make Guesses**: Enter a number between 1-100 and click "Submit Guess"
5. **Get Feedback**: The server will tell you if your guess is "Too High" or "Too Low"
6. **Win Points**: First player to guess correctly gets 1 point
7. **New Round**: Game automatically resets with a new random number
8. **Chat**: Use the chat box to communicate with other players

## 🧪 Testing Multiplayer

To test with multiple players:

1. **Open multiple browser tabs** to `http://localhost:5000`
2. **Create a room** in one tab and note the room code
3. **Join the same room** in other tabs using the room code
4. **Start guessing** - you'll see real-time updates across all tabs
5. **Use the chat** to communicate between players

## 🚀 Deployment Options

### Option 1: Heroku (Recommended for beginners)

1. **Install Heroku CLI** and login:
   ```bash
   # Install from https://devcenter.heroku.com/articles/heroku-cli
   heroku login
   ```

2. **Create Heroku app**:
   ```bash
   heroku create your-game-name
   ```

3. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

4. **Open your app**:
   ```bash
   heroku open
   ```

### Option 2: Render (Free tier available)

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service**
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 app:app`
   - **Environment**: Python 3.11.7

4. **Deploy** - Render will automatically deploy from your repository

### Option 3: Railway

1. **Connect your GitHub repository** to Railway
2. **Railway will auto-detect** the Python app
3. **Deploy** - Railway handles the rest automatically

### Option 4: PythonAnywhere

1. **Upload your files** to PythonAnywhere
2. **Create a new web app** with Flask
3. **Set the working directory** to your project folder
4. **Configure WSGI file** to point to your app
5. **Reload** the web app

## 🔧 Production Configuration

For production deployment, consider these optimizations:

### Environment Variables

Create a `.env` file for local development:
```env
FLASK_ENV=development
FLASK_SECRET_KEY=your-secret-key-here
```

### Production Settings

The app is configured for production with:
- **Gunicorn** as the WSGI server
- **Eventlet** for Socket.IO compatibility
- **Single worker** to avoid Socket.IO conflicts

### Scaling Considerations

- **Current setup**: Single worker (suitable for small to medium games)
- **For larger scale**: Consider Redis for Socket.IO message queue
- **Database**: Current in-memory storage resets on server restart

## 📁 Project Structure

```
guess-the-number/
├── app.py              # Flask backend with Socket.IO and room system
├── templates/
│   └── index.html      # Single HTML page with embedded CSS/JS
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── runtime.txt        # Python version specification
├── render.yaml        # Render deployment configuration
└── README.md          # This file
```

## 🔧 Backend Code Overview

The Flask backend (`app.py`) includes:

- **Room management** with unique 6-character codes
- **Socket.IO event handlers** for real-time communication
- **Player management** (join, leave, score tracking)
- **Game logic** (number generation, guess validation, scoring)
- **Chat system** for player communication
- **API endpoints** for room creation and management

## 🎨 Frontend Features

- **Single HTML page** with embedded CSS and JavaScript
- **Room-based navigation** (welcome, create, join, game screens)
- **Responsive grid layout** that adapts to screen size
- **Real-time updates** for players, scores, and chat
- **Clean, minimal design** with gradient background
- **Keyboard shortcuts** (Enter key for inputs)

## 🐛 Troubleshooting

### Common Issues:

1. **Port already in use**: Change the port in `app.py` line 85
2. **Socket.IO connection failed**: Check if the server is running
3. **Players not updating**: Refresh the browser page
4. **Room not found**: Check the room code spelling

### Deployment Issues:

1. **Heroku build fails**: Check `requirements.txt` and `Procfile`
2. **Socket.IO not working**: Ensure using `eventlet` worker class
3. **App crashes**: Check logs with `heroku logs --tail`

### Debug Mode:

The application runs in debug mode locally. For production, set:
```bash
export FLASK_ENV=production
```

## 🔮 Future Enhancements

This minimal implementation can be expanded with:

- **Persistent database storage** (PostgreSQL, MongoDB)
- **User authentication** and profiles
- **Multiple game modes** (different number ranges, time limits)
- **Tournament system** with brackets
- **Spectator mode** for watching games
- **Sound effects and animations**
- **Mobile app** using React Native or Flutter

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Guessing! 🎯** 