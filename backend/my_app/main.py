from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from core_fun.auth  import get_current_active_user

from orm.session import get_db
from orm.session import SessionLocal
from orm.utils_ORM import get_user
from  api_routes.routers.auth import auth_router
from api_routes.routers.pois import pois_router 
from api_routes.routers.sois import sois_router
from api_routes.routers.aois import aois_router
from api_routes.routers.lois import lois_router 
import uvicorn
# from api.routers.projects import project_router
# from api.routers.ingredients import ingredient_router
# from api.routers.items import item_router
# from api.routers.menus import menu_router
# from api.routers.orders import order_router
# from api.routers.ratings import rating_router

# from core.auth import get_current_active_user
# from app.db.server import create_project, add_project_to_user, get_user
# from app.core.auth import get_current_active_leader, get_current_active_user


app = FastAPI(docs_url="/api/docs", openapi_url="/api")

origins = [
    "http://localhost:3000",
    "http://localhost:3000/api",
    "http://localhost:3000/api/v1",
    "http://localhost:19000",
    "http://10.0.2.2:19000",
    "http://10.0.2.2:5554",
    "http://192.168.56.1:19000",
    "http://192.168.56.1:5554",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")


async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):

    print("here", id)
    user1 = get_user(db, id)
    return user1.email


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


# Routers

app.include_router(
    pois_router,
    prefix="/api/v1",
    tags=["pois"],
    dependencies=[Depends(get_current_active_user)],
    )
app.include_router( 
    sois_router,
    prefix="/api/v1",
    tags=["sois"],
    dependencies=[Depends(get_current_active_user)],
    )
app.include_router(
    aois_router,
    prefix="/api/v1",
    tags=["aois"],
    dependencies=[Depends(get_current_active_user)],
    )

app.include_router(
    lois_router,
    prefix="/api/v1",
    tags=["lois"],
    dependencies=[Depends(get_current_active_user)],
    )

app.include_router(auth_router, prefix="/api", tags=["auth"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

