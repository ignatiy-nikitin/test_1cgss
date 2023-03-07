from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Boolean, BigInteger

from db import Base


class Good(Base):
    __tablename__ = 'goods'

    ref = Column(String(255), nullable=False)
    measure = Column(String(255), nullable=False)
    nomenclature = Column(String(255), nullable=False)
    count = Column(Float, nullable=False)
    orderToProducer = Column(String(255), nullable=True)
    producer = Column(String(255), nullable=True)
    sum = Column(Float, nullable=True)
    sumWithTax = Column(Float, nullable=True)
    order = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False, default=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)

    __mapper_args__ = {
        'primary_key': [ref, nomenclature]
    }


class GoodValidator(BaseModel):
    ref: str
    measure: str | None = ''
    nomenclature: str | None = ''
    count: float = 0.0
    orderToProducer: str | None = ''
    producer: str | None = ''
    sum: float | None = 0.0
    sumWithTax: float | None = 0.0
    order: str | None = ''
    deletionMark: bool = False
    modificationTime: int
