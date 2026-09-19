# AI Chat ✨

A full-stack AI chat application with a gold starfield UI — built with FastAPI and the Gemini API.

**🔗 Live Demo:** https://ai-chat-faah.onrender.com

*(Free hosting — first load may take ~30s to wake up)*

## Features

- 💬 Real conversation memory — full chat history sent with each request
- ⭐ Animated gold particle background (canvas, 250 twinkling stars)
- 🎨 Light / Dark / Auto theme modes with glassmorphism message bubbles
- 📝 Markdown rendering for AI responses
- 🚫 Request cancellation — "New chat" aborts in-flight replies (AbortController)
- ⚠️ Graceful error handling for rate limits and server errors

## Stack

| Layer     | Tech                                   |
|-----------|----------------------------------------|
| Backend   | Python, FastAPI, Uvicorn               |
| AI        | Google Gemini API (`google-genai` SDK) |
| Frontend  | Vanilla HTML / CSS / JavaScript        |
| Deploy    | Render (auto-deploy from GitHub)       |

## Run Locally

```bash
git clone https://github.com/Yasminenaser1/ai-chat.git
cd ai-chat
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-key"   # free key at aistudio.google.com
uvicorn main:app --reload
```


## Architecture

Browser → FastAPI `/chat` endpoint → Gemini API → response rendered as markdown.
The API key lives only in a server-side environment variable — never in code or the client.

---
Built by [Yasmine Naser](https://github.com/Yasminenaser1)
