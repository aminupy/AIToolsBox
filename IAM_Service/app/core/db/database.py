from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings
from sqlalchemy.ext.declarative import declarative_base

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
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

EntityBase = declarative_base()


def init_db() -> bool:
    EntityBase.metadata.create_all(bind=engine)
    return True


def get_entitybase():
    return EntityBase


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()