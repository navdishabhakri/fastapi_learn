from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

class Habits(BaseModel):
    name : str
    description : str | None = None
    created_at : datetime = Field(default_factory= datetime.today) # so that everytime you create a habit, this will run
    
app = FastAPI()
habits=[]
id_count= 1
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/habits", status_code =status.HTTP_201_CREATED)
async def create_habits(habit: Habits): # habit is variable name of type Habits
    global id_count 
    habit_item= habit.model_dump()
    habit_item["id"]= id_count
    habit_item["done"] = False
    id_count+=1
    habits.append(habit_item)
    return habit_item

@app.get("/habits", status_code= status.HTTP_200_OK)
async def get_habits():
    return habits

@app.put("/habits/{id}/complete", status_code= status.HTTP_200_OK)
async def update_habits(id:int):
    found=False
    i=0
    for dicts in habits:
        if dicts["id"]==id:
            found=True
            dicts["done"]= True
            break
        i+=1
    if found==False:
        raise HTTPException(status_code=404, detail="Item not found")
    return habits[i]

@app.delete("/habits/{id}", status_code= status.HTTP_200_OK)
async def delete_habits(id:int):
    found=False
    i=0
    for dicts in habits:
        if dicts["id"]==id:
            found=True
            del habits[i]
            break
        i+=1
        
        
    if found==False:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Successfully deleted {id}"}
    
    
    
    