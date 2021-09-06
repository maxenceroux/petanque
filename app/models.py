from sqlalchemy import Boolean, Column, Integer, Float, String

from database import Base


class Terrain(Base):
    __tablename__ = "terrains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
