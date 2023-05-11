from fastapi import APIRouter
from fastapi import Depends, Response
from orm.session import get_db
from orm.utils_ORM import get_loi_by_id,get_pois_by_id, get_aoi_by_id, create_poi,update_aoi_num_pois
from core_fun.auth import get_current_active_user 
from orm.schema import BasePoisSchema


pois_router = re =  APIRouter()


@re.post("/poi", response_model_exclude_none=True)
async def pois_post_aoi(
        response:Response,
        poi:BasePoisSchema,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    new_poi = create_poi(db,current_user.userId, poi)

    return new_poi 

@re.get("/poi/{poi_id}", response_model_exclude_none=True)
async def poi_get_by_id(
        poi_id:int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user)
):
    poi_by_id = get_pois_by_id(db, poi_id)
    return poi_by_id

