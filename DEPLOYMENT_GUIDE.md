# 🚀 Free Deployment Guide for Guess the Number Game

Since GitHub Pages only supports static sites (HTML/CSS/JS), here are the **best free hosting options** for your multiplayer Flask app:

## 🆓 **Top Free Hosting Options**

### 1. **Railway** (Recommended - Easiest)
**Free Tier**: $5 credit monthly, auto-sleeps when not used

```bash
# 1. Go to https://railway.app
# 2. Sign up with GitHub
# 3. Click "New Project" → "Deploy from GitHub repo"
# 4. Select your repository
# 5. Railway auto-detects Python and deploys!
```

**Why Railway?**
- ✅ Auto-detects Python apps
- ✅ Free tier with $5 credit
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Real-time logs

### 2. **Render** (Great Alternative)
**Free Tier**: 750 hours/month, auto-sleeps

```bash
# 1. Go to https://render.com
# 2. Sign up with GitHub
# 3. Click "New" → "Web Service"
# 4. Connect your GitHub repo
# 5. Configure:
#    - Build Command: pip install -r requirements.txt
#    - Start Command: gunicorn --worker-class eventlet -w 1 app:app
#    - Environment: Python 3.11.7
```

### 3. **Fly.io** (Generous Free Tier)
**Free Tier**: 3 shared-cpu VMs, 3GB persistent volume

```bash
# 1. Install Fly CLI: https://fly.io/docs/hands-on/install-flyctl/
# 2. Sign up: fly auth signup
# 3. Deploy: fly launch
# 4. Follow prompts (auto-detects Python)
```

### 4. **Vercel** (Serverless)
**Free Tier**: 100GB bandwidth, 100 serverless function executions

```bash
# 1. Go to https://vercel.com
# 2. Import your GitHub repo
# 3. Vercel auto-detects Python
# 4. Deploy!
```

### 5. **PythonAnywhere** (Python-Specific)
**Free Tier**: 512MB storage, 1 web app

```bash
# 1. Go to https://www.pythonanywhere.com
# 2. Sign up for free account
# 3. Upload your files
# 4. Create new web app → Flask
# 5. Set working directory to your project
# 6. Configure WSGI file
```

## 🎯 **Quick Deploy Script**

Run this to deploy to Railway (easiest):

```bash
# Make sure you have git initialized
git init
git add .
git commit -m "Initial commit"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main

# Then go to https://railway.app and connect your repo!
```

## 🔧 **Pre-Deployment Checklist**

1. ✅ **All files committed** to git
2. ✅ **requirements.txt** includes all dependencies
3. ✅ **Procfile** (for Heroku) or **railway.json** (for Railway)
4. ✅ **runtime.txt** specifies Python version
5. ✅ **Port configuration** uses environment variables

## 🌐 **Environment Variables**

For production, set these:

```bash
FLASK_ENV=production
FLASK_SECRET_KEY=your-secret-key-here
PORT=8080  # Most platforms set this automatically
```

## 📊 **Platform Comparison**

| Platform | Free Tier | Ease | Auto-Sleep | Custom Domain |
|----------|-----------|------|------------|---------------|
| Railway  | $5/month  | ⭐⭐⭐⭐⭐ | Yes | Yes |
| Render   | 750h/month| ⭐⭐⭐⭐ | Yes | Yes |
| Fly.io   | 3 VMs     | ⭐⭐⭐ | No | Yes |
| Vercel   | 100GB     | ⭐⭐⭐⭐ | Yes | Yes |
| PythonAnywhere | 512MB | ⭐⭐⭐ | No | No |

## 🚨 **Important Notes**

### **Why Not GitHub Pages?**
- ❌ Only supports static sites (HTML/CSS/JS)
- ❌ No server-side processing
- ❌ No WebSocket support (needed for real-time multiplayer)

### **Socket.IO Considerations**
- ✅ **Railway/Render**: Full WebSocket support
- ✅ **Fly.io**: Full WebSocket support  
- ✅ **Vercel**: Limited WebSocket support (serverless)
- ⚠️ **PythonAnywhere**: WebSocket support varies

## 🎮 **Testing Your Deployed App**

1. **Create a room** and get the room code
2. **Share the URL** with friends
3. **Test multiplayer** with different devices
4. **Check real-time features** (chat, scores, game updates)

## 🔗 **Sharing Your Game**

Once deployed, you'll get a URL like:
- Railway: `https://your-app.railway.app`
- Render: `https://your-app.onrender.com`
- Fly.io: `https://your-app.fly.dev`

**Share this URL with friends to play together!**

---

**Recommended: Start with Railway - it's the easiest and most reliable for multiplayer games! 🚀** 