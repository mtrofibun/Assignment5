from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, details):
    db_order_details = models.OrderDetail(
        order_id =details.order_id,
        sandwich_id =details.sandwich_id,
        amount =details.amount
    )
    db.add(db_order_details)
    db.commit()
    db.refresh(db_order_details)
    return db_order_details


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, detail_id):
    return db.query(models.OrderDetail).filter(models.Detail.id == detail_id).first()


def update(db: Session, detail_id, detail):

    db_order_details = db.query(models.OrderDetail).filter(models.Detail.id == detail_id)
    update_data = detail.model_dump(exclude_unset=True)
    db_order_details.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_details.first()


def delete(db: Session, detail_id):
    db_order_details = db.query(models.OrderDetail).filter(models.Detail.id == detail_id)
    db_order_details.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
