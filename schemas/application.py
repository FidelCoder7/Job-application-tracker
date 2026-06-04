from pydantic import BaseModel
from datetime import date
from datetime import datetime
from pydantic import Field

from models.application import ApplicationStatus


class ApplicationBase(BaseModel):
    company_name: str = Field(
        min_length=2,
        max_length=100
    )

    job_title: str = Field(
        min_length=2,
        max_length=100
    )

    location: str | None = None

    status: ApplicationStatus = (
        ApplicationStatus.APPLIED
    )

    application_date: date | None = None

    salary: float | None = None

    job_link: str | None = None

    notes: str | None = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    company_name: str | None = None

    job_title: str | None = None

    location: str | None = None

    status: ApplicationStatus | None = None

    application_date: date | None = None

    salary: float | None = None

    job_link: str | None = None

    notes: str | None = None


class ApplicationResponse(ApplicationBase):
    id: int

    user_id: int

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True
