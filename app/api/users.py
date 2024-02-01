from fastapi import APIRouter, Depends
from dependencies.database import get_db, SessionLocal
from dependencies.auth import Token, create_access_token, get_current_user
from schemas.user import User
from services.users import UserServices
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status

router = APIRouter()


@router.post("/register/", response_model=User,  status_code=status.HTTP_201_CREATED)
async def register(user: User,
                   db: SessionLocal = Depends(get_db)):

    user_service = UserServices(db)
    return user_service.create_new(user)


@router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: SessionLocal = Depends(get_db)):

    user_service = UserServices(db)
    user = user_service.get_user_for_auth(form_data.username, form_data.password)
    access_token = create_access_token(username=user.username, role=user.role)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected-resource/", response_model=User)
async def protected_resource(current_user: User = Depends(get_current_user)):
    return current_user
