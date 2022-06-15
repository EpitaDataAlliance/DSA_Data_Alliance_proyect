from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "postgresql://postgres:1234@localhost/phone_price_db"

engine = create_engine(SQL_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()