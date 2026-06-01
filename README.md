# 🚀 FastAPI Habit Tracker

A small FastAPI project that implements a SQLite-backed habit tracker using **SQLAlchemy** and **Pydantic**.

## ✨ What this project does

- Defines a Habits API with endpoints to create, read, update, and delete habits
- Uses a SQLite database via SQLAlchemy ORM for persistent storage
- Loads the database connection URL from `.env` using `python-dotenv`
- Automatically creates database tables on startup with `Base.metadata.create_all(bind=engine)`
- Provides dependency-managed database sessions for each request

## 🛠️ Tech stack

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- python-dotenv

## 📁 Project files

- `main.py` - main FastAPI application and SQLAlchemy model definitions
- `.env` - environment file containing the SQLite connection URL
- `.venv/` - local Python virtual environment created for the project

## ✅ Setup

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install fastapi uvicorn python-dotenv sqlalchemy
```

## 🔧 Environment configuration

Create or update `.env` with a valid SQLite connection string:

```env
DB=sqlite:////tmp/habits.db
```

> Make sure there is no extra spacing around `=` or quotes in `.env`.

## ▶️ Run the app

Start the app using Uvicorn:

```bash
source .venv/bin/activate
uvicorn main:app --reload
```

If port `8000` is already in use, launch on another port:

```bash
uvicorn main:app --reload --port 8001
```

Then open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 📡 API endpoints

| Method | Endpoint                | Description                | Status Code      |
| ------ | ----------------------- | -------------------------- | ---------------- |
| GET    | `/`                     | Root health-check endpoint | `200 OK`         |
| GET    | `/habits`               | Retrieve all habits        | `200 OK`         |
| POST   | `/habits`               | Create a new habit         | `201 CREATED`    |
| PUT    | `/habits/{id}/complete` | Mark a habit as complete   | `200 OK`         |
| DELETE | `/habits/{id}`          | Delete a habit             | `204 NO CONTENT` |

## 🧪 Example request

Create a new habit:

```bash
curl -X POST http://127.0.0.1:8000/habits \
  -H "Content-Type: application/json" \
  -d '{"name": "Drink Water", "description": "Drink 2 liters of water today"}'
```

Example response:

```json
{
  "id": 1,
  "name": "Drink Water",
  "description": "Drink 2 liters of water today",
  "done": false,
  "created_at": "2026-05-31T23:13:22.940000"
}
```

## 💬 Chatbot API

A streaming chatbot with conversation history powered by **Groq** and **FastAPI**.

### ✨ What it does

- Accepts a user message and maintains full conversation history across turns
- Streams responses token-by-token using Groq's LLaMA 3.3 model
- Stores chat history in-memory per session so the model has context of prior messages
- Exposes a single `POST /api` endpoint that returns a streaming plain-text response

### 🛠️ Tech stack additions

- Groq
- LLaMA 3.3 (via Groq API)

### ▶️ Run the chatbot

```bash
source .venv/bin/activate
uvicorn chatbot/chat:app --port 8001 --reload
```

### 📡 Endpoint

`POST /api`

**Example request:**

```bash
curl -X POST http://127.0.0.1:8001/api \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the capital of France?"}'
```

**Example response** (streamed plain text):

```
The capital of France is Paris.
```

---

## 📝 Developer notes

- The project uses SQLAlchemy ORM models instead of in-memory storage, so habits persist across server restarts.
- `HabitCreate` is a Pydantic model used for request validation on `POST /habits`.
- `Depends(get_session)` ensures each endpoint receives a fresh database session that is cleaned up automatically.
- `.env` syntax must be exact, otherwise `python-dotenv` may fail to parse the DB URL and SQLAlchemy will raise `ArgumentError`.
- Because port `8000` was already occupied in this environment, the app was successfully started on port `8001`.
