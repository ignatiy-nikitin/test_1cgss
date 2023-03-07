from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Text, BigInteger

from db import Base


class DestinationPoint(Base):
    __tablename__ = 'destinationpoint'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    code = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    destinationPointCode = Column(Text, nullable=True)
    additionalInformation = Column(Text, nullable=True)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class DestinationPointValidator(BaseModel):
    ref: str
    code: str = ''
    description: str | None = ''
    deletionMark: bool = False
    destinationPointCode: str | None = ''
    additionalInformation: str | None = ''
    modificationTime: int
