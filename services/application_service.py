from sqlalchemy.orm import Session

from models.application import Application

from schemas.application import (
    ApplicationCreate,
    ApplicationUpdate
)

# Create Application
def create_application(
    db: Session,
    application_data: ApplicationCreate,
    user_id: int
):
    application = Application(
        **application_data.model_dump(),
        user_id=user_id
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application

# Get All Applications
def get_applications(
    db: Session,
    user_id: int
):
    return (
        db.query(Application)
        .filter(Application.user_id == user_id)
        .all()
    ) 
 # Get One Application
def get_application(
    db: Session,
    application_id: int,
    user_id: int
):
    return (
        db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == user_id
        )
        .first()
    )

# Update Application
def update_application(
    db: Session,
    application: Application,
    update_data: ApplicationUpdate
):
    updates = update_data.model_dump(
        exclude_unset=True
    )

    for field, value in updates.items():
        setattr(
            application,
            field,
            value
        )

    db.commit()
    db.refresh(application)

    return application

#  Delete Application
def delete_application(
    db: Session,
    application: Application
):
    db.delete(application)
    db.commit()
