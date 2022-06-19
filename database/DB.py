from lib2to3.pytree import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:0000@localhost/hedi",echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)