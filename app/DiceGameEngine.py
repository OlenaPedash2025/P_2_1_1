import random
from dataclasses import asdict, dataclass, field
from pathlib import Path

from DiceStatistik import DiceStatistik
from StorageStrategy import JSONStorageStrategy, StorageStrategy


@dataclass
class DiceGameEngine:
    sides: int = 6
    storage_tool: StorageStrategy = field(default_factory=JSONStorageStrategy)
    stats: DiceStatistik = field(init=False)

    def __post_init__(self):
        self.stats = DiceStatistik(sides=self.sides)
        self.storage_tool = self.storage_tool

    def roll(self) -> int:
        result = random.randint(1, self.sides)
        self.stats.add_roll(result)
        return result

    def load_from_file(self, file_path: str):
        try:
            data = self.storage_tool.load(file_path)
            if data:
                self.sides = data["sides"]
                self.stats = DiceStatistik(sides=self.sides)
                self.stats.rolls = data["rolls"]
                self.stats.counts = {int(k): v for k, v in data["counts"].items()}
                return True

        except Exception as e:
            print(f"Error occurred while loading file: {e}")
            return False

    def finalize(self, full_path: Path):
        self.storage_tool.save(asdict(self.stats), str(full_path))
