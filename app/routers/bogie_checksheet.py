from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/forms/bogie-checksheet", tags=["Bogie Checksheet"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=schemas.BogieChecksheetOut, status_code=201)
def create_bogie_checksheet(payload: schemas.BogieChecksheetBase, db: Session = Depends(get_db)):
    try:
        created = crud.create_bogie_checksheet(db, payload)
        return {
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": created.formNumber,
                "inspectionBy": created.inspectionBy,
                "inspectionDate": created.inspectionDate.isoformat(),
                "status": "Saved"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
