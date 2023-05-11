# Generate fibonacci sequence up to n
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.types import DateTime,Float,Text,SmallInteger
from sqlalchemy.orm import relationship, backref
from .session import Base


class User(Base):
    __tablename__ = "users"
    userId = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    passwordHash = Column(String)

    pois = relationship("POI", back_populates="user", cascade="all,delete")
    lois = relationship("LOI", back_populates="user", cascade="all,delete")
    aois = relationship("AOI", back_populates="user", cascade="all,delete")
    sois = relationship("SOI", back_populates="user", cascade="all,delete")



    def __repr__(self):

        return f"User(id={self.userId}, email={self.email}, password={self.passwordHash}"



class POI(Base):
    __tablename__ = "POI"
    poiId = Column(Integer, primary_key=True, index=True)
    poiName= Column(String, index=True,nullable=False)
    poiTitle = Column(String)
    keywords = Column(String)
    period= Column(String)
    year = Column(Integer)
    image_url = Column(String)
    description = Column(String)
    description_en = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    height= Column(Float)
    address = Column(String)
    scope = Column(String)
    source = Column(String)
    creator = Column(String)
    publisher = Column(String)
    contributor = Column(String)
    rights = Column(String)
    verif_open = Column(String)


    user_id = Column(Integer, ForeignKey("users.userId"))
    user = relationship("User", back_populates="pois")

    lois = relationship("LOI", back_populates="poi", cascade="all,delete")
    aois = relationship("AOI", back_populates="poi", cascade="all,delete")
    sois = relationship("SOI", back_populates="poi", cascade="all,delete")



    def __repr__(self):
        return f"POI(id={self.poiId}, name={self.poiName}, description={self.description}, latitude={self.latitude}, longitude={self.longitude}, address={self.address})"

class LOI(Base):
    __tablename__ = "LOI"
    routeId= Column(Integer, primary_key=True, index=True)
    routeTitle= Column(String, index=True)
    areaName_en = Column(String, index=True)
    routeUploadTime = Column(DateTime)
    routeDescription = Column(String)
    routeOwner = Column(String)
    coverage= Column(String)
    duration = Column(String)
    transportation = Column(String)
    open = Column(Boolean)



    #Relationship with User Many to One
    user_id = Column(Integer, ForeignKey("users.userId"))
    user = relationship("User", back_populates="lois")

    #Relationship with POI One to Many
    poiId = Column(Integer, ForeignKey("POI.poiId"))
    poi = relationship("POI", back_populates="lois")

    def __repr__(self):
        return f"LOI(id={self.routeId}, name={self.routeTitle}, description={self.routeDescription}" 

class AOI(Base):
    __tablename__ = "AOI"
    aoiId= Column(Integer, primary_key=True, index=True)
    title= Column(String, index=True)
    areaName_en = Column(String, index=True)
    uploadTime = Column(DateTime)
    description = Column(String)
    owner = Column(String)
    coverage= Column(String)
    numPois = Column(Integer)
    open = Column(Boolean)

    #Relationship with User Many to One
    user_id = Column(Integer, ForeignKey("users.userId"))
    user = relationship("User", back_populates="aois")

    #Relationship with AOI One to Many
    poiId = Column(Integer, ForeignKey("POI.poiId"))
    poi = relationship("POI", back_populates="aois")


    

    def __repr__(self):
        return f"AOI(id={self.aoiId}, name={self.areaName_en}, description={self.description}" 

class SOI(Base):
    __tablename__ = "SOI"
    soiId= Column(Integer, primary_key=True, index=True)
    title= Column(String, index=True)
    areaName_en = Column(String, index=True)
    uploadTime = Column(DateTime)
    description = Column(String)
    owner = Column(String)
    identifier = Column(String)
    transportation = Column(String)
    open = Column(Boolean)

    poiId = Column(Integer, ForeignKey("POI.poiId"))
    poi = relationship("POI", back_populates="sois")

    user_id = Column(Integer, ForeignKey("users.userId"))
    user = relationship("User", back_populates="sois")

    def __repr__(self):
        return f"SOI(id={self.soiId}, areaName={self.areaName_en}, description={self.description}"



