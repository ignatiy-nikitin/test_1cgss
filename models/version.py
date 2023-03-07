from pydantic import BaseModel
from sqlalchemy import Column, Text, BigInteger

from db import Base


class Version(Base):
    __tablename__ = 'version'

    model = Column(Text, nullable=False, primary_key=True, unique=True)
    version = Column(BigInteger, nullable=False)


class VersionValidator(BaseModel):
    model: str
    version: int
