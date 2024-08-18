from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.v1.routes.users import user_router
from app.db.database import init_db
from app.core.logging.logger import configure_logger


configure_logger()

init_db()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])

logger.info("IAM Service Started")

@app.get("/")
async def root():
    return {"message": "Hello Dear !"}


