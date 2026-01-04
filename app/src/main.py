from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .config import settings
from .database import engine, Base, get_db
from .models import UserDB
from .schemas import UserSchema
from .redis_client import redis_conn
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    print(f"DEBUG: Full Database URL: {settings.POSTGRES_URL}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/users/{username}")
async def create_user(username: str, user_data: UserSchema, db: AsyncSession = Depends(get_db)):
    # Cache Check
    cached = await redis_conn.get(f"user:{username}")
    if cached:
        return {"status": "from_cache", "email": cached}

    # DB Operation
    new_user = UserDB(username=username, email=user_data.email)
    db.add(new_user)
    await db.commit()
    
    # Set Cache
    await redis_conn.setex(f"user:{username}", 60, user_data.email)
    return {"status": "created", "username": username}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
