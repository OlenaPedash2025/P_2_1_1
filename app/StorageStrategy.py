import json
from abc import ABC, abstractmethod

import dicttoxml
import xmltodict
import yaml


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, data, file_path):
        pass

    @abstractmethod
    def load(self, file_path):
        pass


class StorageContext(StorageStrategy):
    def save(self, data: dict, file_path: str):
        try:
            mode = "wb" if file_path.endswith(".xml") else "w"
            encoding = "utf-8" if mode == "w" else None
            with open(file_path, mode, encoding=encoding) as f:
                content = self._serialize(data)

                f.write(content)
            print(f"Data successfully saved to {file_path}")

        except Exception as e:
            print(f"Error occurred while saving file: {e}")

    def load(self, file_path: str) -> dict:
        try:
            mode = "rb" if file_path.endswith(".xml") else "r"
            encoding = None if mode == "rb" else "utf-8"

            with open(file_path, mode, encoding=encoding) as f:
                content = f.read()
                return self._deserialize(content)
        except Exception as e:
            print(f"Error occurred while loading file: {e}")
            return {}


class JSONStorageStrategy(StorageContext):
    def _serialize(self, data: dict) -> str:
        return json.dumps(data, indent=4)

    def _deserialize(self, content: str) -> dict:
        return json.loads(content)


class YAMLStorageStrategy(StorageContext):
    def _serialize(self, data: dict) -> str:
        return yaml.dump(data, default_flow_style=False)

    def _deserialize(self, content: str) -> dict:
        return yaml.safe_load(content)


class XMLStorageStrategy(StorageContext):
    def _serialize(self, data: dict) -> str:
        return dicttoxml.dicttoxml(data, custom_root="root", attr_type=False)

    def _deserialize(self, content: str) -> dict:
        return xmltodict.parse(content)["root"]


# class JSONStorageStrategy(StorageStrategy):

# def save(self, data: dict, file_path: str):

# try:

# with open(file_path, 'w') as f:

# json.dump(data, f)

# except Exception as e:

# print(f"Error occurred while saving JSON file: {e}")


# def load(self, file_path: str) -> dict:

# try:

# with open(file_path, 'r') as f:

# return json.load(f)

# except Exception:

# return {}


# class YAMLStorageStrategy(StorageStrategy):

# def save(self, data: dict, file_path: str):

# try:

# with open(file_path, 'w') as f:

# yaml.dump(data, f)

# except Exception as e:

# print(f"Error occurred while saving YAML file: {e}")


# def load(self, file_path: str) -> dict:

# try:

# with open(file_path, 'r') as f:

# return yaml.safe_load(f)

# except Exception:

# return {}


# class XMLStorageStrategy(StorageStrategy):

# def save(self, data: dict, file_path: str):

# try:

# xml_data = dicttoxml.dicttoxml(data, custom_root='root', attr_type=False)

# with open(file_path, 'wb') as f:

# f.write(xml_data)

# except Exception as e:

# print(f"Error occurred while saving XML file: {e}")


# def load(self, file_path: str) -> dict:

# try:

# with open(file_path, 'rb') as f:

# xml_data = f.read()

# return xmltodict.parse(xml_data)['root']

# except Exception:

# return {}
