from enum import Enum


class ApplicationStatus(str, Enum):
    APPLIED = "Applied"
    ASSESSMENT = "Assessment"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"
    ACCEPTED = "Accepted"
    WITHDRAWN = "Withdrawn"

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy import Enum as SQLAlchemyEnum

from sqlalchemy.orm import relationship

from database.database import Base

from datetime import datetime

class Application(Base):
    __tablename__ = "applications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_name = Column(
        String,
        nullable=False
    )

    job_title = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=True
    )

    status = Column(
        SQLAlchemyEnum(ApplicationStatus),
        default=ApplicationStatus.APPLIED,
        nullable=False
    )

    application_date = Column(
        Date,
        nullable=True
    )

    salary = Column(
        Float,
        nullable=True
    )

    job_link = Column(
        String,
        nullable=True
    )

    notes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="applications"
    )


