
import jwt
from jwt import PyJWTError
from orm.models import User
from orm.utils_ORM import get_user_by_email, create_user 
from orm.schema import CreateUserSchema, TokenDataSchema,TokenSchema
from fastapi import Depends, HTTPException, status
from . import security
from orm import session


def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not security.verify_password(password, user.passwordHash):
        return False
    return user


def sign_up_new_user(db, email: str, password: str):

    user = get_user_by_email(db, email)
    if user:
        return False  # User already exists
    new_user = create_user(
        db,
        CreateUserSchema(
            email=email,
            password=password,
            is_active=True,
        ),
    )
    return new_user


async def get_current_user(
    db=Depends(session.get_db), token: str = Depends(security.oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,security.SECRET_KEY ,algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenDataSchema(email=email)
    except PyJWTError:
        raise credentials_exception
    user = get_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: User= Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    print("Current User ==>",current_user.email)
    return current_user
