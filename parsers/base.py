import json
import os
import re
from abc import ABC, abstractmethod
from typing import Type, NamedTuple
from xml.etree import ElementTree

from loguru import logger
from sqlalchemy import inspect
from sqlalchemy import update, insert

from models.version import Version


class BaseFilesHandler(ABC):
    @property
    @abstractmethod
    def reg(self):
        pass

    @property
    @abstractmethod
    def model_version_name(self):
        pass

    @property
    @abstractmethod
    def xml_file_parse_class(self):
        pass

    def __init__(self, dir_path: str, db):
        self.dir_path = dir_path
        self.db = db
        files_paths = os.listdir(self.dir_path)

        model_version_db = self.db.query(Version).get(self.model_version_name)
        self.model_version_timestamp = int(model_version_db.version) if model_version_db else 0
        logger.debug(f'self.model_version_timestamp = {self.model_version_timestamp}')

        self.files_handler_files_paths = [fp for fp in files_paths if re.compile(self.reg).match(fp)]

        logger.debug(
            f'BaseFilesHandler: {self.__class__}\n'
            f'\tRegex: {self.reg}\n'
            f'\tModel version name: {self.model_version_name}\n'
            f'\tLast model version modification in db: {self.model_version_timestamp}\n'
            f'\tAll files count: {len(self.files_handler_files_paths)}'
            f'\tAll files names found: {self.files_handler_files_paths}'
        )

        self.files_names_to_modification_time = {f: self._get_file_modification_timestamp(f) for f in
                                                 self.files_handler_files_paths}

        logger.debug(
            f'\tFiles names to modification time: \n'
            f'{json.dumps(self.files_names_to_modification_time, indent=4, ensure_ascii=False)}'
        )

        # filter filenames, where time of modification more than version in db
        self.files_handler_files_paths = list(
            filter(lambda f: self.files_names_to_modification_time[f] > self.model_version_timestamp,
                   self.files_handler_files_paths)
        )
        # sort filenames by time of modification
        self.files_handler_files_paths = sorted(
            self.files_handler_files_paths, key=lambda f: self.files_names_to_modification_time[f]
        )

        logger.debug(
            f'\tFiles filtered more than last time modification and sorted by modification time (this files '
            f'will be added): \n\t{self.files_handler_files_paths}'
        )

        self.file_modification_time_updated_by_file = None

    def _get_file_modification_timestamp(self, file_name: str) -> int:
        file_name = file_name.split('.')[0]
        return int(file_name.split('_')[1])

    def parse_files(self):
        for file_name in self.files_handler_files_paths:
            full_file_path = os.path.join(self.dir_path, file_name)
            file_modification_time = self.files_names_to_modification_time[file_name]
            self.xml_file_parse_class(full_file_path, self.db, file_modification_time).parse_file()
            self._update_model_version_time(file_name)
            logger.info(f'File parsed: {file_name}')

    def _update_model_version_time(self, file_name: str):
        db_model_version = self.db.query(Version).filter(Version.model == self.model_version_name).first()
        logger.debug(f'db_model_version = {db_model_version}')
        if db_model_version is None:
            version_model = Version(
                model=self.model_version_name,
                version=self.files_names_to_modification_time[file_name],
            )
            self.db.add(version_model)
        else:
            db_model_version.version = self.files_names_to_modification_time[file_name]
        self.file_modification_time_updated_by_file = self.files_names_to_modification_time[file_name]


class NestedXmlFileParserObject(NamedTuple):
    parent_to_child_params_pass: dict[str, str]
    xml_tag_name: str
    parser_class: Type['BaseNestedXmlFileParser']


class BaseXmlFileParser(ABC):
    @property
    @abstractmethod
    def db_model_fields_to_xml_fields(self):
        pass

    @property
    @abstractmethod
    def db_model(self):
        pass

    @property
    @abstractmethod
    def xml_tag_name(self):
        pass

    @property
    @abstractmethod
    def validator_model(self):
        pass

    nested_objects: list[NestedXmlFileParserObject] = []

    def __init__(self, file_path: str, db, file_modification_time: int):
        self.file_path = file_path
        self.db = db
        self.file_modification_time = file_modification_time
        self.pk_field = inspect(self.db_model).primary_key[0].name

        self.tree = ElementTree.parse(self.file_path)
        self.root = self.tree.getroot()
        if self.xml_tag_name is not None:
            self.xml_file_data = self.root.findall(self.xml_tag_name)
        else:
            self.xml_file_data = None

    def _get_model_data_to_save(self, f_data):
        model_data_to_save = {}
        for model_field, xml_field in self.db_model_fields_to_xml_fields.items():
            try:
                model_data_to_save[model_field] = f_data.find(xml_field).text
            except AttributeError:
                pass

        model_data_to_save['modificationTime'] = self.file_modification_time

        return model_data_to_save

    def _convert_model_data_to_save_to_python_types(self, model_data_to_save: dict):
        try:
            return self.validator_model(**model_data_to_save).dict()
        except Exception as e:
            logger.error(f'Pydantic model convert error (model: {self.validator_model}), \n'
                         f'data: {model_data_to_save}')
            raise e

    def _save_data_to_db(self, model_data_to_save: dict):
        self.db.execute(insert(self.db_model), model_data_to_save)

    def _update_data_to_db(self, model_data_to_save: dict, pk_field, pk_value):
        self.db.execute(
            update(self.db_model).where(
                getattr(self.db_model, pk_field) == pk_value).values(model_data_to_save)
        )

    def _save_or_update_data_to_db(self, model_data_to_save: dict):
        try:
            pk_value = model_data_to_save[self.pk_field]
            db_record = self.db.query(self.db_model).get(pk_value)
            if db_record:
                logger.trace(f'Ref: {pk_value} found, update record of model: {self.db_model}...')
                self._update_data_to_db(model_data_to_save, self.pk_field, pk_value)
            else:
                self._save_data_to_db(model_data_to_save)
        except Exception as e:
            logger.error(f'Ошибка при добавлении записи. Класс: {self.db_model},\n'
                         f'\tФайл: {self.file_path},\n'
                         f'\tДанные: {model_data_to_save},\n'
                         f'\tМодель: \n'
                         f'\tСообщение исключения: {e}')
            raise e

    def parse_file(self):
        for f_data in self.xml_file_data:
            if f_data is None:
                continue

            model_data_to_save = self._get_model_data_to_save(f_data)
            model_data_to_save = self._convert_model_data_to_save_to_python_types(model_data_to_save)
            self._save_or_update_data_to_db(model_data_to_save)

            for nested_object in self.nested_objects:
                nested_object_xml_data = f_data.findall(nested_object.xml_tag_name)
                nested_object.parser_class(
                    self.file_path, self.db, self.file_modification_time, nested_object_xml_data, model_data_to_save,
                    nested_object.parent_to_child_params_pass,
                ).parse_file()


class BaseNestedXmlFileParser(BaseXmlFileParser, ABC):
    xml_tag_name = None
    xml_file_starts_with = None

    def __init__(self, file_path, db, file_modification_time, xml_file_data, parent_model_data,
                 parent_to_child_params_pass):
        super().__init__(file_path, db, file_modification_time)
        self.xml_file_data = xml_file_data
        self.parent_model_data = parent_model_data
        self.parent_to_child_params_pass = parent_to_child_params_pass

        logger.debug(f'BaseNestedXmlFileParser: {self.__class__}, xml_file_data count: {len(self.xml_file_data)}')

    def _get_model_data_to_save(self, f_data):
        model_data_to_save = super()._get_model_data_to_save(f_data)
        for parent_param, child_param in self.parent_to_child_params_pass.items():
            model_data_to_save[child_param] = self.parent_model_data[parent_param]
        return model_data_to_save
