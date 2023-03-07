from models.order_to_producer import OrderToProducer, OrderToProducerValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class OrderToProducerXmlFileParser(BaseXmlFileParser):
    db_model = OrderToProducer
    validator_model = OrderToProducerValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'description': 'Description',
        'owner': 'Owner',
        'parent': 'Parent',
        'code': 'Code',
        'organization': 'Организация',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/CatalogObject.ДоговорыКонтрагентов'


class OrderToProducerFilesHandler(BaseFilesHandler):
    reg = 'ДоговорыКонтрагентов_[0-9]*.xml'
    model_version_name = 'PARTNER_CONTRACT'
    xml_file_parse_class = OrderToProducerXmlFileParser
