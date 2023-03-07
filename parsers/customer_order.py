from models.customer_order import CustomerOrder, CustomerOrderValidator
from parsers.base import BaseXmlFileParser, BaseFilesHandler, NestedXmlFileParserObject
from parsers.goods import GoodOrderNestedXmlFileParser


class CustomerOrderXmlFileParser(BaseXmlFileParser):
    db_model = CustomerOrder
    validator_model = CustomerOrderValidator
    db_model_fields_to_xml_fields = {
        'ref': 'Ref',
        'number': 'Number',
        'date': 'Date',
        'comment': 'Комментарий',
        'principal': 'Принципал',
        'responsible': 'Ответственный',
        'isInAccounting': 'ОтражатьВБухгалтерскомУчете',
        'isInTaxAccounting': 'ОтражатьВНалоговомУчете',
        'sum': 'СуммаДокумента',
        'contactPartnerPerson': 'КонтактноеЛицоКонтрагента',
        'project': 'Проект',
        'customerOrder': 'ЗаявкаПокупателя',
        'client': 'Заказчик',
        'genContractor': 'Генподрядчик',
        'subContractor': 'Субподрядчик',
        'organization': 'Организация',
        'consignee': 'Грузополучатель',
        'partner': 'Контрагент',
        'deletionMark': 'DeletionMark',
    }
    xml_tag_name = './/DocumentObject.ЗаказПокупателя'
    nested_objects = [
        NestedXmlFileParserObject(
            parent_to_child_params_pass={
                'ref': 'ref',
                'modificationTime': 'modificationTime',
            },
            xml_tag_name='Товары/Row',
            parser_class=GoodOrderNestedXmlFileParser,
        )
    ]


class CustomerOrderFilesHandler(BaseFilesHandler):
    reg = 'ЗаказПокупателя_[0-9]*.xml'
    model_version_name = 'CUSTOMERORDER'
    xml_file_parse_class = CustomerOrderXmlFileParser
