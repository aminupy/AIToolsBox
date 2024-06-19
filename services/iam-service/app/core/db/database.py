from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

try:
    if not database_exists(engine.url):
        logger.info("Creating Database")
        create_database(engine.url)
        logger.info("Database Created")

except Exception as e:
    logger.error(f"Error: {e}")

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
logger.info("Database Session Created")

EntityBase = declarative_base()


def init_db() -> bool:
    EntityBase.metadata.create_all(bind=engine)
    logger.info("Database Initialized")
    return True


def get_entitybase():
    return EntityBase


@logger.catch
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
