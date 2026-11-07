from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def read_root():
    return {"message": "Welcome to my E-commerce Backend API!"}
@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    return {"status": "Database session successfully established!"}

@app.post("/items/")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return(db_item)

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items