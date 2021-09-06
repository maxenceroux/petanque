from sqlalchemy.orm import Session

import models, schemas


def get_terrain(db: Session, terrain_id: str):
    return db.query(models.Terrain).filter(models.Terrain.id == terrain_id).first()


def get_terrains(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Terrain).offset(skip).limit(limit).all()


def create_terrain(db: Session, terrain: schemas.TerrainSchema):
    model_terrain = models.Terrain(
        name=terrain.name, latitude=terrain.latitude, longitude=terrain.longitude
    )
    db.add(model_terrain)
    db.commit()
    db.refresh(model_terrain)
    return model_terrain
