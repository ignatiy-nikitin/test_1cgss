from pydantic import BaseModel
from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class OrderToProducer(Base):
    """Продукция."""

    __tablename__ = 'ordertoproducer'

    ref: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False)
    deletionMark: Mapped[bool] = mapped_column()
    modificationTime = Column(BigInteger, nullable=False, default=1560944029)


class OrderToProducerValidator(BaseModel):
    ref: str
    deletionMark: bool
    modificationTime: int
