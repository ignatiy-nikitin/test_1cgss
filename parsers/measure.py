from models.measure import Measure, MeasureValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class MeasureXmlFileParser(BaseXmlFileParser):
    db_model = Measure
    validator_model = MeasureValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'code': 'Code',
        'description': 'Description',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/CatalogObject.ЕдиницыИзмерения'


class MeasureFilesHandler(BaseFilesHandler):
    reg = 'ЕдиницыИзмерения_[0-9]*.xml'
    model_version_name = 'MEASURE'
    xml_file_parse_class = MeasureXmlFileParser
