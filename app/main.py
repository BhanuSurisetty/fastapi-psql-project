from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from .database import SessionLocal, engine
from . import shemas
from . import models
from . import crud

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add_user", response_model=shemas.UserOut)
def add_user(user: shemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/get_users", response_model=list[shemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
