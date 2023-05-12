from turtle import title
from pydantic import BaseModel
from datetime import datetime
import typing as t

class BaseUserSchema(BaseModel):
    email:str
    is_active:bool = True

class CreateUserSchema(BaseUserSchema):
    password:str
    class Config:
        orm_mode = True


class TokenSchema(BaseModel):
    access_token:str
    token_type:str
class TokenDataSchema(BaseModel):
    email:str

#Pois Schema 

class BasePoisSchema(BaseModel):
    poiName:str
    poiTitle:str
    keywords:str = None
    period:str = None
    year:int
    image_url:str = None
    description:str
    description_en:str = None
    latitude:float
    longitude:float
    height:float  
    address:str = None
    scope:str = None
    source:str 
    creator:str 
    publisher:str 
    rights:str = None
    verif_open:str = None

class CreatePoisSchema(BasePoisSchema):
    poiId:int
    aois:t.List["CreateAoiSchema"] = []
    lois:t.List["CreateLoiSchema"] = []
    sois:t.List["CreateSoiSchema"] = []
    class Config:
        orm_mode = True

class BaseAoiSchema(BaseModel):
    title:str
    areaName_en:str = None
    uploadTime:datetime
    description:str
    owner:str
    coverage:str = None
    numPois:int
    open:bool

class CreateAoiSchema(BaseAoiSchema):
    aoiId:int
    class Config:
        orm_mode = True

class BaseLoiSchema(BaseModel):
    routeTitle:str
    areaName_en:str = None
    routeUploadTime:datetime
    routeDescription:str
    routeOwner:str
    coverage:str = None
    duration:str = None
    transportation:str = None
    open:bool

class CreateLoiSchema(BaseLoiSchema):
    loiId:int
    class Config:
        orm_mode = True

class BaseSoiSchema(BaseModel):
    title:str
    areaName_en:str = None
    uploadTime:datetime
    description:str
    owner:str
    identifier:str
    transportation:str
    open:bool

class CreateSoiSchema(BaseSoiSchema):
    soiId:int
    class Config:
        orm_mode = True

class UserSchema(BaseUserSchema):
    userId:int
    class Config:
        orm_mode = True


