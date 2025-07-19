from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/forms/wheel-specifications", tags=["Wheel Specifications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=schemas.WheelSpecOut, status_code=201)
def create_wheel_spec(spec: schemas.WheelSpecBase, db: Session = Depends(get_db)):
    created = crud.create_wheel_spec(db, spec)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": created
    }

@router.get("", response_model=schemas.WheelSpecListOut)
def get_wheel_specs(
    formNumber: str = Query(None),
    submittedBy: str = Query(None),
    submittedDate: str = Query(None),
    db: Session = Depends(get_db)
):
    results = crud.get_filtered_wheel_specs(db, formNumber, submittedBy, submittedDate)
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": results
    }
