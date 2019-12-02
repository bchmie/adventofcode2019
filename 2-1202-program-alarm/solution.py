import os
from typing import List

INPUT_FILE = 'input.txt'


def operation(state: List[int], cursor: int) -> None:
    opcode = state[cursor]

    i1, i2 = state[cursor + 1], state[cursor + 2]
    v1, v2 = state[i1], state[i2]

    if opcode == 1:
        result = v1 + v2
    elif opcode == 2:
        result = v1 * v2
    else:
        raise ValueError(f'Invalid opcode {opcode} at pos {cursor}.')

    target_index = state[cursor + 3]

    state[target_index] = result


def compute(state: List[int]) -> List[int]:
    cursor = 0
    while state[cursor] != 99:
        operation(state, cursor)
        cursor += 4

    return state


def main() -> int:
    input_path = os.path.join(
        os.path.dirname(__file__), INPUT_FILE
    )

    with open(input_path, 'r') as f:
        content = f.readline()
        initial_state = [int(i) for i in content.split(',')]

    i, j, i_next = 0, 0, True

    while True:
        state = list(initial_state)  # copy initial state
        state[1], state[2] = i, j
        compute(state)
        if state[0] == 19690720:
            break
        else:
            if i_next:
                i += 1
            else:
                j += 1
            i_next = not i_next

    return 100 * i + j


if __name__ == '__main__':
    print(main())
