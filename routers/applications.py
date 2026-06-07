from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from database.database import get_db

from models.user import User

from schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse
)

from core.dependencies import get_current_user

from services.application_service import (
    create_application,
    get_applications,
    get_application,
    update_application,
    delete_application
)


router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


# CREATE
@router.post(
    "",
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_application(
        db,
        application_data,
        current_user.id

    )


# GET ALL
@router.get(
    "",
    response_model=list[ApplicationResponse]
)
def get_all_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_applications(
        db,
        current_user.id
    )


# GET ONE
@router.get(
    "/{application_id}",
    response_model=ApplicationResponse
)
def get_single_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    application = get_application(
        db,
        application_id,
        current_user.id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


# UPDATE
@router.put(
    "/{application_id}",
    response_model=ApplicationResponse
)
def update_existing_application(
    application_id: int,
    update_data: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    application = get_application(
        db,
        application_id,
        current_user.id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return update_application(
        db,
        application,
        update_data
    )


# DELETE
@router.delete(
    "/{application_id}"
)
def delete_existing_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    application = get_application(
        db,
        application_id,
        current_user.id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    delete_application(
        db,
        application
    )

    return {
        "message": "Application deleted"
    }
