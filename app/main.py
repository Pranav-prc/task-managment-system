from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.tasks import router as tasks_router

app = FastAPI(title="Task Management System")

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Task Management System API is running!"}
