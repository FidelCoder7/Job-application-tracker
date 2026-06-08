from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.database import get_db

from core.dependencies import (
    get_current_user
)

from models.user import User

from schemas.dashboard import (
    DashboardStats
)

from services.dashboard_service import (
    get_dashboard_stats
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/stats",
    response_model=DashboardStats
)
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_dashboard_stats(
        db,
        current_user.id
    )
