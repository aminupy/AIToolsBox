from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database
from loguru import logger

from app.core.config import get_settings

config = get_settings()

# Generate Database URL
DATABASE_URL = (
    f"{config.DATABASE_DIALECT}://"
    f"{config.DATABASE_USERNAME}:"
    f"{config.DATABASE_PASSWORD}@"
    f"{config.DATABASE_HOSTNAME}:"
    f"{config.DATABASE_PORT}/"
    f"{config.DATABASE_NAME}"
)

engine = create_engine(DATABASE_URL, echo=config.DEBUG_MODE, future=True)

EntityBase = declarative_base()


def init_db() -> bool:
    EntityBase.metadata.create_all(bind=engine)
    logger.info("Database Initialized")
    return True


try:
    if not database_exists(engine.url):
        logger.info("Creating Database")
        create_database(engine.url)
        logger.info("Database Created")

except Exception as e:
    logger.error(f"Error: {e}")

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
logger.info("Database Session Created")


def get_entitybase():
    return EntityBase


def get_db() -> Generator[Session, None, None]:
    db = session_local()
    try:
        yield db
    except SQLAlchemyError as ex:
        logger.error(f"Database error during session: {ex}")
        db.rollback()  # Roll back any uncommitted transactions
        raise  # Re-raise the original exception for further handling
    finally:
        db.close()