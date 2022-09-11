from pydantic import BaseModel
from typing import Dict, List

class Fidata(BaseModel):
    value: int
    unit: str

class FilterData(BaseModel):
    type: str
    value: str
    operator: str

class DataLifeSpan(BaseModel):
    value: int
    unit: str

class PurposeforDetail(BaseModel):
    Category: Dict[str, str]
    code: str
    text: str
    refUri: str

class ConsentDetail(BaseModel):
    consentStart: str
    consentExpiry: str
    Customer: Dict[str, str]
    FIDataRange: Dict[str, str]
    consentMode: str
    consentTypes: List[str] = []
    fetchType: str
    DataConsumer: Dict[str, str]
    fiTypes: list = []
    redirectUrl: str

class SessionData(BaseModel):
    consentId: str =  None
    fromdate: str
    todate: str
    format: str
