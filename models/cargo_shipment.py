import datetime

from pydantic import BaseModel, validator
from sqlalchemy import Column, String, Date, Boolean, BigInteger

from db import Base


class CargoShipment(Base):
    __tablename__ = 'cargoshipment'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    date = Column(Date, nullable=True)
    number = Column(String(255), nullable=True)
    documentStatus = Column(String(255), nullable=True)
    partner = Column(String(255), nullable=True)
    organization = Column(String(255), nullable=True)
    responsiblePerson = Column(String(255), nullable=True)
    baseDocument = Column(String(255), nullable=True)
    shippedDate = Column(String(255), nullable=True)
    arrivedDate = Column(String(255), nullable=True)
    project = Column(String(255), nullable=True)
    shipper = Column(String(255), nullable=True)
    consignee = Column(String(255), nullable=True)
    shippedPoint = Column(String(255), nullable=True)
    consigneePoint = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class CargoShipmentValidator(BaseModel):
    ref: str
    date: datetime.date
    number: str | None
    documentStatus: str | None
    partner: str | None
    organization: str | None
    responsiblePerson: str | None
    baseDocument: str | None
    shippedDate: str | None
    arrivedDate: str | None
    project: str | None
    shipper: str | None
    consignee: str | None
    shippedPoint: str | None
    consigneePoint: str | None
    deletionMark: bool
    modificationTime: int

    @validator('date', pre=True)
    def parse_date(cls, value):
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S').date()
