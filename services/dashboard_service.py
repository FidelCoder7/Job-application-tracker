from sqlalchemy.orm import Session

from models.application import (
    Application,
    ApplicationStatus
)


def get_dashboard_stats(
    db: Session,
    user_id: int
):
    applications = (
        db.query(Application)
        .filter(
            Application.user_id == user_id
        )
        .all()
    )

    total = len(applications)

    applied = 0
    assessment = 0
    interview = 0
    offer = 0
    accepted = 0
    rejected = 0
    withdrawn = 0

    for app in applications:

        if app.status == ApplicationStatus.APPLIED:
            applied += 1

        elif app.status == ApplicationStatus.ASSESSMENT:
            assessment += 1

        elif app.status == ApplicationStatus.INTERVIEW:
            interview += 1

        elif app.status == ApplicationStatus.OFFER:
            offer += 1

        elif app.status == ApplicationStatus.ACCEPTED:
            accepted += 1

        elif app.status == ApplicationStatus.REJECTED:
            rejected += 1

        elif app.status == ApplicationStatus.WITHDRAWN:
            withdrawn += 1

    success_rate = 0

    if total > 0:
        success_rate = round(
            ((offer + accepted) / total) * 100,
            2
        )

    return {
        "total_applications": total,
        "applied": applied,
        "assessment": assessment,
        "interview": interview,
        "offer": offer,
        "accepted": accepted,
        "rejected": rejected,
        "withdrawn": withdrawn,
        "success_rate": success_rate
    }
