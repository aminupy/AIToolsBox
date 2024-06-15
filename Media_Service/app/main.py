from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints.media import media_router

app = FastAPI()

origins = ["http://localhost", "http://ocr"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(media_router, prefix="/api/v1/media", tags=["media"])


@app.get("/")
async def root():
    return {"message": "Hello From Media Service !"}
