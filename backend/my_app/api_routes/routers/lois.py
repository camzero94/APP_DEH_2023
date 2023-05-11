from fastapi import APIRouter
from fastapi import Depends, Response
from orm.session import get_db
from core_fun.auth import get_current_active_user 
from orm.schema import BaseLoiSchema 
from orm.utils_ORM import create_loi ,get_pois_by_id, get_loi_by_id, get_loi_by_user


lois_router = re =  APIRouter()


@re.post("/loi", response_model_exclude_none=True)
async def loi_post(
        response:Response,
        poi_id:int,
        loi:BaseLoiSchema,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)):

    poi = get_pois_by_id(db, poi_id)
    new_loi = create_loi(db,current_user.userId,poi.poiId ,loi)
    poi.aois.append(new_loi)
    return f"Succesfully Creates LOI New Loi=> {new_loi}"

@re.get("/loi/{loi_id}", response_model_exclude_none=True)
async def loi_get_by_id(
        loi_id:int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    aoi_by_id = get_loi_by_id(db, loi_id)
    return aoi_by_id

@re.get("/lois_list", response_model_exclude_none=True)
async def lois_get_list(
        response:Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    lois_by_user = get_loi_by_user(db, current_user.userId)
    response.headers["Content-Range"] = f"0-9/{len(lois_by_user)}"
    response.headers["Acces-Control-Headers"] = "Content-Range"

    return lois_by_user


