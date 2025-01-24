from fastapi import FastAPI
# from src.backend.models import Task  
# from src.backend.database import add_task, get_tasks 

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

