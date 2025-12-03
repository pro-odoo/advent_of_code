demo = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")

def compute_joltage(bank: str, digits: int) -> int:
    total = ""
    start = 0
    for digit in reversed(range(digits)):
        biggest = 0
        if digit != 0:
            biggest = max(bank[start:-digit])
        else:
            biggest = max(bank[start:])
        start = bank[start:].index(biggest) + 1 + start
        total += biggest
    return int(total)

def count_part1(banks):
    return sum([compute_joltage(bank, 2) for bank in banks])


def count_part2(banks):
    return sum([compute_joltage(bank, 12) for bank in banks])

if __name__ == "__main__":
    with open("./input03.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        print(count_part1(demo))  # 357
        print(count_part1(lines)) # 17613
        print(count_part2(demo))  # 3121910778619
        print(count_part2(lines)) # 17613

