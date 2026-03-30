from dataclasses import dataclass, field


@dataclass
class DiceStatistik:
    sides: int = 6
    rolls: int = 0
    counts: dict[int, int] = field(init=False)

    def __post_init__(self):
        self.counts = {i: 0 for i in range(1, self.sides + 1)}

    def add_roll(self, result: int):
        self.rolls += 1
        self.counts[result] += 1

    def get_distribution(self) -> dict[int, float]:
        if self.rolls == 0:
            return {i: 0.0 for i in range(1, self.sides + 1)}
        return {i: self.counts[i] / self.rolls for i in range(1, self.sides + 1)}
