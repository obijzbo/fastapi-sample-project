from fastapi import FastAPI
from tasks import create_task
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client["celery_db"]
collection = db["task_results"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI with Celery and Docker Compose"}

@app.post("/tasks/{data}")
def run_task(data: str):
    task = create_task.delay(data)
    return {"task_id": task.id, "status": "Processing"}

@app.get("/tasks/")
def get_all_tasks():
    tasks = list(collection.find({}, {"_id": 0}))
    return {"tasks": tasks}

<<<<<<< HEAD
# commented
=======
#main . py

>>>>>>> 6d9a51c7a80fdb1a0ca3114c4fede42b2cd7e3eb
