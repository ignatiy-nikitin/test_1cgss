from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DEBUG

engine = create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


class Base(DeclarativeBase):
    pass


def create_all_db_tables():
    if DEBUG:
        from models.goods import Good
        from models.order_to_producer import OrderToProducer
        from models.measure import Measure
        from models.nomenclature import Nomenclature
        from models.customer_order import CustomerOrder
        from models.partner import Partner
        from models.cargo_shipment import CargoShipment
        from models.project import Project
        from models.destination_point import DestinationPoint
        from models.version import Version
        Base.metadata.create_all(bind=engine)
