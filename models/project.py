from pydantic import BaseModel
from sqlalchemy import Column, Text, String, Boolean, BigInteger

from db import Base


class Project(Base):
    __tablename__ = 'project'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    code = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    parent = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class ProjectValidator(BaseModel):
    ref: str
    code: str | None = ''
    description: str | None = ''
    parent: str | None = ''
    deletionMark: bool
    modificationTime: int
