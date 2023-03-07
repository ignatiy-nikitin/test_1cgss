import datetime

from pydantic import BaseModel, validator
from sqlalchemy import Column, Text, String, Date, Boolean, Float, BigInteger

from db import Base


class CustomerOrder(Base):
    __tablename__ = 'customerorder'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    number = Column(String(255), nullable=True)
    date = Column(Date, nullable=True)
    comment = Column(Text, nullable=True)
    principal = Column(String(255), nullable=True)
    responsible = Column(String(255), nullable=True)
    isInAccounting = Column(Boolean, nullable=True)
    isInTaxAccounting = Column(Boolean, nullable=True)
    sum = Column(Float, nullable=True)
    contactPartnerPerson = Column(String(255), nullable=True)
    project = Column(String(255), nullable=True)
    customerOrder = Column(String(255), nullable=True)
    client = Column(String(255), nullable=True)
    genContractor = Column(String(255), nullable=True)
    subContractor = Column(String(255), nullable=True)
    organization = Column(String(255), nullable=True)
    consignee = Column(String(255), nullable=True)
    partner = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class CustomerOrderValidator(BaseModel):
    ref: str
    number: str | None
    date: datetime.date | None
    comment: str | None
    principal: str | None
    responsible: str | None
    isInAccounting: bool | None
    isInTaxAccounting: bool | None
    sum: float | None
    contactPartnerPerson: str | None
    project: str | None
    customerOrder: str | None
    client: str | None
    genContractor: str | None
    subContractor: str | None
    organization: str | None
    consignee: str | None
    partner: str | None
    deletionMark: bool
    modificationTime: int

    @validator('date', pre=True)
    def parse_date(cls, value):
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S').date()
