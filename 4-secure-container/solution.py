from collections import Counter


START = 146810
STOP = 612564


def is_valid_password(num: int) -> bool:
    num = str(num)
    for i, c in enumerate(num[:-1]):
        if int(c) > int(num[i+1]):
            return False
    for i, c in enumerate(num[:-1]):
        if c == num[i+1]:
            break
    else:
        return False
    counter = Counter(str(num))
    if 2 not in counter.values():
        return False

    return True


def main() -> int:
    solution = 0
    for i in range(START, STOP):
        if is_valid_password(i):
            solution += 1
    return solution


if __name__ == '__main__':
    print(main())
