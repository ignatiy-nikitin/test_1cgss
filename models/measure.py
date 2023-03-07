from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, BigInteger

from db import Base


class Measure(Base):
    """Продукция."""

    __tablename__ = 'measure'

    ref = Column(String(255), primary_key=True, unique=True, nullable=False)
    code = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    deletionMark = Column(Boolean, nullable=False)
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class MeasureValidator(BaseModel):
    ref: str
    code: str | None = ''
    description: str | None = ''
    deletionMark: bool
    modificationTime: int
