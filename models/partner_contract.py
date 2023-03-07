from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Text, BigInteger

from db import Base


class PartnerContract(Base):
    __tablename__ = 'partnercontract'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    code = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    organization = Column(String(255), nullable=True)
    owner = Column(String(255), nullable=True)
    parent = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class PartnerContractValidator(BaseModel):
    ref: str
    code: str | None = ''
    description: str | None = ''
    organization: str | None = ''
    owner: str | None = ''
    parent: str | None = ''
    deletionMark: bool
    modificationTime: int
