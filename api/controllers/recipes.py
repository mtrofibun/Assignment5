from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, recipes):
    db_recipe= models.Recipe(
        resource_id =recipes.resource_id,
        sandwich_id =recipes.sandwich_id,
        amount =recipes.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe_id == recipe_id).first()


def update(db: Session, recipe_id, detail):

    db_recipe = db.query(models.Recipe).filter(models.Recipe_id == recipe_id)
    update_data = detail.model_dump(exclude_unset=True)
    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()


def delete(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe_id == recipe_id)
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
