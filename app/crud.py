from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def create_wheel_spec(db: Session, spec: schemas.WheelSpecBase):
    existing = db.query(models.WheelSpecification).filter_by(formNumber=spec.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Form with formNumber '{spec.formNumber}' already exists.")
    db_spec = models.WheelSpecification(**spec.dict())
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_filtered_wheel_specs(db: Session, formNumber=None, submittedBy=None, submittedDate=None):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    return query.all()

def create_bogie_checksheet(db: Session, data: schemas.BogieChecksheetBase):
    existing = db.query(models.BogieChecksheet).filter_by(formNumber=data.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Checksheet with formNumber '{data.formNumber}' already exists.")
    db_checksheet = models.BogieChecksheet(**data.dict())
    db.add(db_checksheet)
    db.commit()
    db.refresh(db_checksheet)
    return db_checksheet
