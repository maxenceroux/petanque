from typing import List, Optional


from pydantic import BaseModel


class TerrainSchema(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class TerrainsSchema(BaseModel):
    terrains: List[TerrainSchema]

    class Config:
        orm_mode = True
