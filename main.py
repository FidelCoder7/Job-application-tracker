from fastapi import FastAPI

from routers.auth import router as auth_router
from routers.applications import router as applications_router
from routers.dashboard import router as dashboard_router

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
