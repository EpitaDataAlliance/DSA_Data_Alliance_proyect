from DB import Base, engine
from models import Item

print("Creating DB..")

Base.metadata.create_all(engine)