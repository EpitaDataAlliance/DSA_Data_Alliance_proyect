from database import SessionLocal
from models import Item

db = SessionLocal()

def insert_phone(new_phone:Item) -> int:
    db.add(new_phone)
    db.flush()
    db.commit()
    return new_phone
