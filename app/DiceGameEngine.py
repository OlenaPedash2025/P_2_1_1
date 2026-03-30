from DiceStatistik import DiceStatistik


import random
from dataclasses import dataclass, field


@dataclass
class DiceGameEngine():
    sides: int = 6
    stats: DiceStatistik = field(init=False)

    def __post_init__(self):
        self.stats = DiceStatistik(sides=self.sides)

    def roll(self) -> int:
        result = random.randint(1, self.sides)
        self.stats.add_roll(result)
        return result   