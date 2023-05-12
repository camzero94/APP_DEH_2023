from sqlalchemy.orm import Session
from .schema import CreateUserSchema,BaseSoiSchema,BaseAoiSchema,CreateSoiSchema,BaseLoiSchema,BasePoisSchema,CreateAoiSchema,CreateLoiSchema,CreatePoisSchema
from .models import User,POI,SOI,AOI,LOI
from fastapi import HTTPException

from core_fun import security

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: CreateUserSchema):
    pasword_hash = security.get_password_hash(user.password)
    db_user = User(email=user.email, passwordHash=pasword_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.userId == user_id).first()

def get_pois_by_id(db: Session, pois_id: int) -> CreatePoisSchema:
    poi = db.query(POI).filter(POI.poiId == pois_id).first()
    if not poi:
        raise HTTPException(status_code=404, detail="POI not found")
    return poi




#SOI util functions 
def create_soi(db: Session, userId: int, soi: BaseSoiSchema):
    new_soi = SOI(
        title=soi.title,
        areaName_en=soi.areaName_en,
        uploadTime=soi.uploadTime,
        description=soi.description,
        owner=soi.owner,
        identifier=soi.identifier,
        transportation=soi.transportation,
        open=soi.open,
        user_id=userId
    )
    db.add(new_soi)
    db.commit()
    db.refresh(new_soi)
    return new_soi

def get_soi_by_id(db: Session, soi_id: int):

    soi = db.query(SOI).filter(SOI.soiId == soi_id).first()
    if soi is None:
        raise HTTPException(status_code=404, detail="SOI not found")
    return soi

def get_soi_by_user(db: Session, user_id: int):
    sois = db.query(SOI).filter(SOI.user_id == user_id).all()
    if not sois:
        raise HTTPException(status_code=404, detail="SOI not found")
    return sois

#AOI util functions
def create_aoi(db: Session, userId: int, poi_id:int,aoi: BaseAoiSchema):
    new_aoi = AOI(
        title=aoi.title,
        areaName_en=aoi.areaName_en,
        uploadTime=aoi.uploadTime,
        description=aoi.description,
        owner=aoi.owner,
        coverage=aoi.coverage,
        numPois=len(aoi.pois),
        open=aoi.open,
        user_id=userId,
        poiId=poi_id,
    )
    db.add(new_aoi)
    db.commit()
    db.refresh(new_aoi)
    return new_aoi

def get_aoi_by_id(db: Session, aoi_id: int):
    aoi = db.query(AOI).filter(AOI.aoiId == aoi_id).first()
    if not aoi:
        raise HTTPException(status_code=404, detail="AOI not found")
    return aoi

def get_aoi_by_user(db: Session, user_id: int):
    aois = db.query(AOI).filter(AOI.user_id == user_id).all()
    if not aois:
        raise HTTPException(status_code=404, detail="AOIS not found")
    return aois


#LOI util functions
def create_loi(db: Session, userId: int, poi_id:int,loi: BaseLoiSchema):
    new_loi = LOI(
        routeTitle=loi.routeTitle,
        areaName_en=loi.areaName_en,
        routeUploadTime=loi.routeUploadTime,
        routeDescription=loi.routeDescription,
        routeOwner=loi.routeOwner,
        coverage=loi.coverage,
        duration=loi.duration,
        transportation=loi.transportation,
        open=loi.open,
        user_id=userId,
        poiId=poi_id,
    )
    db.add(new_loi)
    db.commit()
    db.refresh(new_loi)
    return new_loi

def get_loi_by_id(db: Session, loi_id: int):
    loi = db.query(LOI).filter(LOI.loiId == loi_id).first()

    if not loi:
        raise HTTPException(status_code=404, detail="LOI not found")
    return loi

def get_loi_by_user(db: Session, user_id: int):
    lois = db.query(LOI).filter(LOI.user_id == user_id).all()
    if not lois:
        raise HTTPException(status_code=404, detail="LOIS not found")
    return lois

#POI utils functions

def create_poi(db: Session, userId: int, poi: BasePoisSchema):
    new_poi = POI(
        poiName=poi.poiName,
        poiTitle=poi.poiTitle,
        keywords=poi.keywords,
        period=poi.period,
        year=poi.year,
        description=poi.description,
        description_en=poi.description_en,
        latitude=poi.latitude,
        longitude=poi.longitude,
        height=poi.height,
        address=poi.address,
        scope=poi.scope,
        source=poi.source,
        creator=poi.creator,
        publisher=poi.publisher,
        rights=poi.rights,
        verif_open=poi.verif_open,
        user_id=userId,
    )
    db.add(new_poi)
    db.commit()
    db.refresh(new_poi)
    return new_poi


def update_aoi_num_pois(db: Session, aoi: CreateAoiSchema):
    aoi.numPois = aoi.numPois + 1
    db.commit()
    db.refresh(aoi)
    return aoi


