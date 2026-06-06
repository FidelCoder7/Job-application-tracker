from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from database.database import get_db

from schemas.user import UserCreate
from schemas.user import UserResponse

from schemas.token import Token


from services.auth_service import (
    create_user,
    get_user_by_email,
    authenticate_user
)

from core.security import create_access_token

from core.dependencies import get_current_user

from models.user import User
from fastapi.security import OAuth2PasswordRequestForm

# Router
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Register Endpoint
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return create_user(
        db,
        user_data
    )

# User Login
@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        form_data.username,   # username field will contain email
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# Current User Endpoint
@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user
