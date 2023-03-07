from models.cargo_shipment import CargoShipment, CargoShipmentValidator
from parsers.base import BaseXmlFileParser, NestedXmlFileParserObject, BaseFilesHandler
from parsers.goods import GoodOrderNestedXmlFileParser


class CargoShipmentXmlFileParser(BaseXmlFileParser):
    db_model = CargoShipment
    validator_model = CargoShipmentValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'date': 'Date',
        'number': 'Number',
        'documentStatus': 'СтатусДокумента',
        'partner': 'Контрагент',
        'organization': 'Организация',
        'responsiblePerson': 'Ответственный',
        'baseDocument': 'ЗаказПокупателя',
        'shippedDate': 'ДатаОтгрузки',
        'arrivedDate': 'ДатаПолучения',
        'project': 'Проект',
        'shipper': 'Грузоотправитель',
        'consignee': 'Грузополучатель',
        'shippedPoint': 'ПунктОтправления',
        'consigneePoint': 'ПунктНазначения',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/DocumentObject.ОтгрузкаПокупателю'
    nested_objects = [
        NestedXmlFileParserObject(
            parent_to_child_params_pass={
                'ref': 'ref',
                'modificationTime': 'modificationTime',
            },
            xml_tag_name='ТоварыОтгруженные/Row',
            parser_class=GoodOrderNestedXmlFileParser,
        )
    ]


class CargoShipmentHandler(BaseFilesHandler):
    reg = 'ОтгрузкаПокупателю_[0-9]*.xml'
    model_version_name = 'CARGOSHIPMENT'
    xml_file_parse_class = CargoShipmentXmlFileParser
