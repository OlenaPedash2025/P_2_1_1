from datetime import datetime
from pathlib import Path

from StorageStrategy import (
    JSONStorageStrategy,
    StorageStrategy,
    XMLStorageStrategy,
    YAMLStorageStrategy,
)


class SaveManager:
    SAVE_DIR = Path("saves")
    _STRATEGIES = {
        "json": JSONStorageStrategy(),
        "yaml": YAMLStorageStrategy(),
        "xml": XMLStorageStrategy(),
    }

    def __init__(self):
        self.storage_strategy: StorageStrategy = JSONStorageStrategy()

    @staticmethod
    def _ensure_dir():
        SaveManager.SAVE_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_strategy(key: str):
        clean_key = key.lower().lstrip(".")
        return SaveManager._STRATEGIES.get(clean_key)

    @staticmethod
    def construct_filepath(extension: str) -> Path:
        SaveManager._ensure_dir()
        ts = datetime.now().strftime("%Y%m%d_%H%M")
        return SaveManager.SAVE_DIR / f"save_{ts}.{extension.lstrip('.')}"

    @staticmethod
    def get_all_saves():
        SaveManager._ensure_dir()
        saves = []
        for ext in ["*.json", "*.yaml", "*.xml"]:
            saves.extend(SaveManager.SAVE_DIR.glob(ext))
        return sorted(saves, key=lambda x: x.stat().st_mtime, reverse=True)
