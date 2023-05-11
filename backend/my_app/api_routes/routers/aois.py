
from fastapi import APIRouter
from fastapi import Depends, Response
from orm.session import get_db
from core_fun.auth import get_current_active_user 
from orm.schema import BaseAoiSchema
from orm.utils_ORM import create_aoi ,get_pois_by_id, get_aoi_by_id,get_aoi_by_user
from fastapi import HTTPException


aois_router = re =  APIRouter()


@re.post("/aoi/{poi_id}", response_model_exclude_none=True)
async def aois_post(
        response:Response,
        poi_id:int,
        aoi:BaseAoiSchema,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    poi = get_pois_by_id(db, poi_id)
    new_aoi = create_aoi(db,current_user.userId,poi.poiId,aoi)
    poi.aois.append(new_aoi)

    return f"Succesfully Creates AOI New Aoi=> {new_aoi}"

@re.get("/aoi/{aoi_id}", response_model_exclude_none=True)
async def aoi_get_by_id(
        aoi_id:int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    aoi_by_id = get_aoi_by_id(db, aoi_id)
    return aoi_by_id

@re.get("/aois_list", response_model_exclude_none=True)
async def aois_get_list(
        response:Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    aois_by_user = get_aoi_by_user(db, current_user.userId)
    response.headers["Content-Range"] = f"0-9/{len(aois_by_user)}"
    response.headers["Acces-Control-Headers"] = "Content-Range"

    return aois_by_user


