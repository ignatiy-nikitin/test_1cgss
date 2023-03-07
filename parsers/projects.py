from models.project import Project, ProjectValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler


class ProjectXmlFileParser(BaseXmlFileParser):
    db_model = Project
    validator_model = ProjectValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'parent': 'Parent',
        'code': 'Code',
        'description': 'Description',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/CatalogObject.Проекты'


class ProjectFilesHandler(BaseFilesHandler):
    reg = 'Проекты_[0-9]*.xml'
    model_version_name = 'PROJECT'
    xml_file_parse_class = ProjectXmlFileParser
