from fastapi import FastAPI,status, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from dotenv import load_dotenv


load_dotenv() # loads variables from .env
db_key= os.getenv("DB")

engine = create_engine(db_key) # connects to a SQLite file
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # session so that app talks with db 
Base = declarative_base() # base class that models inherit from

class Habits(Base):
    __tablename__ = 'Habits'
    id = Column(Integer, primary_key = True,nullable=False) # can't be null
    name = Column(String(70), unique = True,nullable=False)
    description = Column(String(100))
    done = Column(Boolean, default = False) 
    created_at= Column(DateTime, default=datetime.utcnow) # so that everytime you create a habit, this will run

Base.metadata.create_all(bind=engine)  # this creates table when app starts

class HabitCreate(BaseModel): # needed because you can only pass a Pydantic model in the 
    name: str
    description : str | None = None
    
app = FastAPI()

def get_session():
    with SessionLocal() as session: #  creates a new database session
        yield session # comes back to close that session
        
# SessionDep = Annotated[Session, Depends(get_session)] # will be written as a parameter so that get_session runs before the endpoint

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Without Depends, FastAPI doesn't know that get_session is a dependency to run automatically before the endpoint.
@app.post("/habits", status_code =status.HTTP_201_CREATED)
async def create_habits(habit: HabitCreate, session: Session = Depends(get_session)): # can only pass pydantic objects here
    db_habit= Habits(name= habit.name, description= habit.description )
    # session.add(habit) # not allowed as it is a pydantic object, session needs a SQLAlchemy object
    session.add(db_habit)
    session.commit()
    session.refresh(db_habit)
    return db_habit

@app.get("/habits", status_code= status.HTTP_200_OK)
async def get_habits(session: Session = Depends(get_session)):
    habit= session.query(Habits).all()
    return habit

@app.put("/habits/{id}/complete", status_code= status.HTTP_200_OK)
async def update_habits(id:int,session: Session=  Depends(get_session)):
    habit= session.get(Habits, id)
    if not habit:
        raise HTTPException(status_code=404, detail="Item not found")
    habit.done= True 
    session.commit() #saves
    session.refresh(habit) # syncs
    return habit


@app.delete("/habits/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_habits(id:int, session: Session = Depends(get_session)):
    habit= session.get(Habits, id)
    if not habit:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(habit)
    session.commit()

    
    
    
    
