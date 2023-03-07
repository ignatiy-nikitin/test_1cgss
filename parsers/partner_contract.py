from models.partner_contract import PartnerContractValidator, PartnerContract
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class PartnerContractXmlFileParser(BaseXmlFileParser):
    db_model = PartnerContract
    validator_model = PartnerContractValidator
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


class PartnerContractFilesHandler(BaseFilesHandler):
    reg = 'ДоговорыКонтрагентов_[0-9]*.xml'
    model_version_name = 'PARTNER_CONTRACT'
    xml_file_parse_class = PartnerContractXmlFileParser
