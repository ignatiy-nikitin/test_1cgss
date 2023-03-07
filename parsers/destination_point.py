from models.destination_point import DestinationPoint, DestinationPointValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class DestinationPointXmlFileParser(BaseXmlFileParser):
    db_model = DestinationPoint
    validator_model = DestinationPointValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'deletionMark': 'DeletionMark',
        'code': 'Code',
        'description': 'Description',
        'destinationPointCode': 'КодПунктаНазначения',
        'additionalInformation': 'ДополнительнаяИнформация',
    }
    xml_tag_name = './/CatalogObject.ПунктыНазначения'


class DestinationPointFilesHandler(BaseFilesHandler):
    reg = 'ПунктыНазначения_[0-9]*.xml'
    model_version_name = 'DESTINATION'
    xml_file_parse_class = DestinationPointXmlFileParser
