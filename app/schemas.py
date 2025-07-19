from pydantic import BaseModel
from typing import Dict, List
from datetime import date

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecificationOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date

    class Config:
        orm_mode = True

class WheelSpecOut(BaseModel):
    success: bool
    message: str
    data: WheelSpecificationOut

class WheelSpecRecord(BaseModel):
    id: int
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

    class Config:
        orm_mode = True

class WheelSpecListOut(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecRecord]

class BogieChecksheetBase(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: Dict[str, str]
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]

class BogieChecksheetOut(BaseModel):
    success: bool
    message: str
    data: Dict[str, str]