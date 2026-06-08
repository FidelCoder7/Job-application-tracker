from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_applications: int

    applied: int
    assessment: int
    interview: int
    offer: int
    accepted: int
    rejected: int
    withdrawn: int

    success_rate: float
