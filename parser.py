from typing import Type

from db import SessionLocal
from parsers.base import BaseFilesHandler
from parsers.cargo_shipment import CargoShipmentHandler
from parsers.customer_order import CustomerOrderFilesHandler
from parsers.destination_point import DestinationPointFilesHandler
from parsers.measure import MeasureFilesHandler
from parsers.nomenclature import NomenclatureFilesHandler
from parsers.order_to_producer import OrderToProducerFilesHandler
from parsers.partner import PartnerFilesHandler
from parsers.partner_contract import PartnerContractFilesHandler
from parsers.projects import ProjectFilesHandler

files_handlers: list[Type[BaseFilesHandler]] = [
    ProjectFilesHandler,
    NomenclatureFilesHandler,
    MeasureFilesHandler,
    PartnerFilesHandler,
    CustomerOrderFilesHandler,  # + Goods
    DestinationPointFilesHandler,
    CargoShipmentHandler,  # + Goods
    PartnerContractFilesHandler,
    OrderToProducerFilesHandler,
]


def parse_xml_files_dir(files_dir_path):
    with SessionLocal() as db:
        for file_handler in files_handlers:
            file_handler(files_dir_path, db).parse_files()
        db.commit()
