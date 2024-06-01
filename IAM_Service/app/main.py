from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db.database import init_db
from app.api.v1.endpoints.users import user_router

init_db()
app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Hello Dear !"}

