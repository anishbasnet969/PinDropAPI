from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db


router = APIRouter(prefix="/flyers", tags=["Flyers"])


@router.get("/", response_model=List[schemas.Flyer])
def get_flyers(db: Session = Depends(get_db)):
    flyers = db.query(models.Flyer).all()
    return flyers


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Flyer)
def create_flyer(
    flyer: schemas.FlyerCreate,
    db: Session = Depends(get_db),
):
    new_flyer = models.Flyer(**flyer.model_dump())
    db.add(new_flyer)
    db.commit()
    db.refresh(new_flyer)

    return new_flyer


@router.get("/{id}", response_model=schemas.Flyer)
def get_flyer(id: int, db: Session = Depends(get_db)):
    flyer = db.query(models.Flyer).filter(models.Flyer.id == id).first()

    if not flyer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Flyer with id: {id} doesn't exist.",
        )

    return flyer


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_flyer(id: int, db: Session = Depends(get_db)):
    flyer_query = db.query(models.Flyer).filter(models.Flyer.id == id)

    if flyer_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Flyer with id: {id} doesn't exist.",
        )

    flyer_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Flyer)
def update_post(
    id: int, updated_flyer: schemas.FlyerCreate, db: Session = Depends(get_db)
):
    flyer_query = db.query(models.Flyer).filter(models.Flyer.id == id)

    flyer = flyer_query.first()

    if flyer == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )

    flyer_query.update(updated_flyer.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(flyer)

    return flyer
