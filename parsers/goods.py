from models.goods import Good, GoodValidator
from parsers.base import BaseNestedXmlFileParser


class GoodOrderNestedXmlFileParser(BaseNestedXmlFileParser):
    db_model = Good
    validator_model = GoodValidator
    update_if_pk_field_found = False
    db_model_fields_to_xml_fields = {
        'measure': 'ЕдиницаИзмерения',
        'nomenclature': 'Номенклатура',
        'count': 'Количество',
        'orderToProducer': 'ЗаказПоставщику',
        'order': 'Заказ',
        'producer': 'Поставщик',
        'sum': 'Сумма',
        'sumWithTax': 'СуммаНДС',
        'deletionMark': 'DeletionMark'
    }

    def _save_or_update_data_to_db(self, model_data_to_save: dict):
        self.db.query(self.db_model).filter(
            self.db_model.ref == model_data_to_save['ref'],
        ).delete()
        self._save_data_to_db(None, model_data_to_save)
