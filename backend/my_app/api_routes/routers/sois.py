from fastapi import APIRouter
from fastapi import Depends, Response
from orm.session import get_db
from orm.utils_ORM import create_soi , get_soi_by_id, get_soi_by_user,get_pois_by_id
from core_fun.auth import get_current_active_user 
from orm.schema import BaseSoiSchema 
from fastapi import HTTPException

sois_router = re =  APIRouter()


@re.post("/sois/{poi_id}", response_model_exclude_none=True)
async def sois_post(
        soi:BaseSoiSchema,
        poi_id:int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    poi = get_pois_by_id(db, poi_id)
    new_soi = create_soi(db, current_user.userId,poi.poiId,soi) 
    poi.aois.append(new_soi)
    return f"Succesfully Creates POI New Poi=> {new_soi}"

@re.get("/soi/{soi_id}", response_model_exclude_none=True)
async def soi_get_by_id(
        response:Response,
        soi_id:int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    soi_by_id = get_soi_by_id(db, soi_id)
    if not soi_by_id:
        raise HTTPException(status_code=404, detail="SOI not found")

    return soi_by_id

@re.get("/sois_list", response_model_exclude_none=True)
async def sois_get_list(
        response:Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    sois_by_user = get_soi_by_user(db, current_user.userId)
    response.headers["Content-Range"] = f"0-9/{len(sois_by_user)}"
    response.headers["Acces-Control-Headers"] = "Content-Range"

    return sois_by_user


