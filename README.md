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

- `file.py` - main FastAPI application and SQLAlchemy model definitions
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
uvicorn file:app --reload
```

If port `8000` is already in use, launch on another port:

```bash
uvicorn file:app --reload --port 8001
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

## 📝 Developer notes

- The project uses SQLAlchemy ORM models instead of in-memory storage, so habits persist across server restarts.
- `HabitCreate` is a Pydantic model used for request validation on `POST /habits`.
- `Depends(get_session)` ensures each endpoint receives a fresh database session that is cleaned up automatically.
- `.env` syntax must be exact, otherwise `python-dotenv` may fail to parse the DB URL and SQLAlchemy will raise `ArgumentError`.
- Because port `8000` was already occupied in this environment, the app was successfully started on port `8001`.

## 💡 Notes

- `file.py` is the application entrypoint and defines the FastAPI app as `app`.
- If you want to preserve data in a different location, update the `DB` value in `.env` to point to a new SQLite file path.
- Use the built-in Swagger docs to explore and test the API interactively.

A small FastAPI project that implements a SQLite-backed habit tracker using SQLAlchemy and Pydantic.

## What was done

- Created a local Python virtual environment in `.venv`
- Installed required dependencies: `fastapi`, `uvicorn`, `python-dotenv`, and `sqlalchemy`
- Added a FastAPI app in `file.py` with endpoints to create, read, update, and delete habit records
- Created a SQLAlchemy ORM model for `Habits`
- Used `python-dotenv` to load the database URL from `.env`
- Fixed `.env` syntax to ensure the DB connection string is parsed correctly
- Verified the app imports and runs successfully
- Launched the Uvicorn server on port `8001` when port `8000` was already occupied

## Files

- `file.py` - main FastAPI application and SQLAlchemy model definitions
- `.env` - environment variable file containing the SQLite connection URL
- `.venv/` - local Python virtual environment (created automatically)

## Setup

1. Open the project folder in a terminal
2. Create the virtual environment:

```bash
python3 -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
python3 -m pip install fastapi uvicorn python-dotenv sqlalchemy
```

## Environment

Ensure `.env` contains the SQLite URL in this format:

```env
DB=sqlite:////tmp/habits.db
```

## Run the app

Start the FastAPI server with:

```bash
uvicorn file:app --reload
```

If port `8000` is in use, run on an alternate port:

```bash
uvicorn file:app --reload --port 8001
```

## Endpoints

- `GET /` - health check
- `POST /habits` - create a new habit
- `GET /habits` - list all habits
- `PUT /habits/{id}/complete` - mark a habit complete
- `DELETE /habits/{id}` - remove a habit

## Notes

- The app uses SQLite via SQLAlchemy and creates tables automatically on startup.
- The server was confirmed to run successfully after fixing `.env` and installing dependencies.
