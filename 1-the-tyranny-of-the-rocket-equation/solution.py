import os
from typing import Sequence

INPUT_FILE = 'input.txt'


def total_fuel(masses: Sequence[int]) -> int:
    return sum(required_fuel(mass) for mass in masses)


def required_fuel(mass: int) -> int:
    return mass // 3 - 2


def main() -> int:
    input_path = os.path.join(
        os.path.dirname(__file__), INPUT_FILE
    )

    with open(input_path, 'r') as f:
        masses = (int(line) for line in f.readlines())

    total = total_fuel(masses)
    return total


if __name__ == '__main__':
    print(main())
