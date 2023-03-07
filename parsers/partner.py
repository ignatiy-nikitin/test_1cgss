from models.partner import Partner, PartnerValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class PartnerXmlFileParser(BaseXmlFileParser):
    db_model = Partner
    validator_model = PartnerValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'description': 'Description',
        'inn': 'ИНН',
        'kpp': 'КПП',
        'fullName': 'НаименованиеПолное',
        'mainPartner': 'ГоловнойКонтрагент',
        'mainManager': 'ОсновнойМенеджерПокупателя',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/CatalogObject.Контрагенты'


class PartnerFilesHandler(BaseFilesHandler):
    reg = 'Контрагенты_[0-9]*.xml'
    model_version_name = 'PARTNER'
    xml_file_parse_class = PartnerXmlFileParser

