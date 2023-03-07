from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Text, BigInteger

from db import Base


class Partner(Base):
    __tablename__ = 'partner'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    inn = Column(String(255), nullable=True)
    kpp = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    fullName = Column(Text, nullable=True)
    mainPartner = Column(String(255), nullable=True)
    mainManager = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class PartnerValidator(BaseModel):
    ref: str
    inn: str | None = ''
    kpp: str | None = ''
    description: str | None = ''
    fullName: str | None = ''
    mainPartner: str | None = ''
    mainManager: str | None = ''
    deletionMark: bool
    modificationTime: int
