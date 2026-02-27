### AI Prompt Manager – Backend Setup Notes (Day 1)

### ✅ What We Completed

- Docker setup (PostgreSQL + FastAPI + NGINX)
- Async SQLAlchemy configuration
- Clean project structure
- Model registration using Base.metadata
- Alembic setup for migrations
- Environment-based configuration (no hardcoded DB URLs)
- Fixed async + Alembic greenlet issue


### 🏗 Project Architecture (So Far)

- Internet
  - → NGINX (reverse proxy)
  - → FastAPI (Gunicorn + Uvicorn workers)
  - → PostgreSQL
- All containerized using Docker Compose.

### 📁 Project Structure

```text
textapp/
├── core/
│ └── database.py
├── models/
│ ├── user.py
│ └── init.py
├── main.py
alembic/
alembic.ini
docker-compose.yml
Dockerfile
.env
```

### 🧠 Key Concepts Learned

#### 1️⃣ Async SQLAlchemy

We used:
- Python create_async_engine()
- async_sessionmaker()

Why async?
- FastAPI runs on ASGI
- Async prevents blocking while waiting for DB
- Uses asyncpg driver

#### 2️⃣ Base = declarative_base()

- Base.metadata stores all table definitions
- Models register themselves when imported
- Alembic reads Base.metadata for migrations

Important:
- If a model is not imported → it won’t be detected.

#### 3️⃣ models/init.py Pattern

```python
from .user import User
all = ["User"]
```

Why?
- Central model registry
- Alembic imports app.models
- Scalable when adding new models

#### 4️⃣ Environment Variables Flow

```text
.env
→ load_dotenv()
→ os.getenv()
→ DATABASE_URL
→ SQLAlchemy engine
```

Never hardcode secrets.

#### 5️⃣ Alembic Migration Setup

We:
- Initialized Alembic
- Connected it to Base.metadata
- Loaded DATABASE_URL from environment
- Replaced async driver for Alembic

Important Fix:
- SYNC_DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

Why?
- Alembic runs in sync mode.
- Async driver causes MissingGreenlet error.