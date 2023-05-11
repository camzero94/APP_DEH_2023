
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from orm.session import get_db
from core_fun.auth import sign_up_new_user
from core_fun import security
from core_fun.auth import authenticate_user

auth_router = r = APIRouter()


@r.post("/token")
async def login(db=Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()):
    # form_data.username == user.email
    #Authentication via email and password
    user = authenticate_user(db,form_data.username,form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"}
        )
    access_token_expires = timedelta(minutes=security.ACESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub":user.email,"id":user.userId},
        expire_delta=access_token_expires
    )

    return {"access_token":access_token, "token_type":"bearer"}


@r.post("/signup")
async def signup(
    db=Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    print("here")
    print(form_data.username, form_data.password)
    user = sign_up_new_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=security.ACESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = security.create_access_token(
        data={"sub": user.email,"id":user.userId},
        expire_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


    
          
