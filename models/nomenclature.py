from pydantic import BaseModel
from sqlalchemy import Column, Text, String, Boolean, BigInteger

from db import Base


class Nomenclature(Base):
    __tablename__ = 'nomenclature'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    fullName = Column(Text, nullable=True)
    reportUnit = Column(String(255), nullable=True)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class NomenclatureValidator(BaseModel):
    ref: str
    description: str | None = ''
    deletionMark: bool
    fullName: str | None = ''
    reportUnit: str | None = ''
    modificationTime: int
