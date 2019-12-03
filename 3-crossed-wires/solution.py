import os

INPUT_FILE = 'input.txt'
STARTING_POINT = (0, 0)


def path_to_points(path):
    x, y = STARTING_POINT
    points = [STARTING_POINT]
    for move in path:
        direction, shift = move[0], int(move[1:])

        for i in range(shift):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            points.append((x, y))

    return points


def main() -> int:
    input_path = os.path.join(
        os.path.dirname(__file__), INPUT_FILE
    )
    with open(input_path, 'r') as f:
        w = f.readline().split(',')
        w1 = f.readline().split(',')

    w_points = path_to_points(w)
    w1_points = path_to_points(w1)
    crossings = [x for x in w_points if x in w1_points]

    distances = []
    for crossing in crossings[1:]:
        x, y = crossing
        distances.append(abs(x) + abs(y))

    return min(distances)


if __name__ == '__main__':
    print(main())
