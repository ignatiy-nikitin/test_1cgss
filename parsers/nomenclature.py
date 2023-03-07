from models.nomenclature import Nomenclature, NomenclatureValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class NomenclatureXmlFileParser(BaseXmlFileParser):
    db_model = Nomenclature
    validator_model = NomenclatureValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'description': 'Description',
        'fullName': 'НаименованиеПолное',
        'reportUnit': 'ЕдиницаДляОтчетов',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/CatalogObject.Номенклатура'


class NomenclatureFilesHandler(BaseFilesHandler):
    reg = 'Номенклатура_[0-9]*.xml'
    model_version_name = 'NOMENCLATURE'
    xml_file_parse_class = NomenclatureXmlFileParser
