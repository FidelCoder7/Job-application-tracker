from fastapi import FastAPI

from database.database import Base
from database.database import engine

from models import User
from models import Application


from routers.auth import router as auth_router
from routers.applications import router as applications_router
from routers.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Application Tracker",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(applications_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": "Job Application Tracker API"
    }
