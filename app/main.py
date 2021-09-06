from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/terrain", response_model=schemas.TerrainSchema)
def create_terrain(
    terrain: schemas.TerrainSchema,
    db: Session = Depends(get_db),
):
    db_terrain = crud.get_terrain(db, terrain_id=terrain.id)
    if db_terrain:
        raise HTTPException(status_code=400, detail="Terrain already in db")
    return crud.create_terrain(db=db, terrain=terrain)


@app.get("/terrain/{terrain_id}", response_model=schemas.TerrainSchema)
def get_terrain(terrain_id: int, db: Session = Depends(get_db)):
    model_terrain = crud.get_terrain(db, terrain_id=terrain_id)
    if model_terrain is None:
        raise HTTPException(status_code=404, detail="Terrain not found")
    return model_terrain


@app.get("/terrains")
def get_terrains(db: Session = Depends(get_db)):
    return crud.get_terrains(db=db)
