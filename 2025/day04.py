demo = [list(line) for line in """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")]


def is_paper_roll(array, x, y):
    if 0 <= x < len(array) and 0 <= y < len(array[0]):
        return array[x][y] == "@"
    return False


def count_around(array, x, y):
    around = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
              (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    return sum([1 if is_paper_roll(array, x, y) else 0 for (x,y) in around])


def count_part1(array):
    count = 0
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] != "@":
                continue
            nbr = count_around(array, x, y)
            if nbr < 4:
                count+=1
    return count


def count_part2(array):
    count = 0
    while True:
        round_count = 0
        next_array = []
        for x in range(len(array)):
            next_array.append([])
            for y in range(len(array[0])):
                if array[x][y] != "@":
                    next_array[x].append(array[x][y])
                    continue
                nbr = count_around(array, x, y)
                if nbr < 4:
                    next_array[x].append(".")
                    round_count += 1
                else:
                    next_array[x].append("@")
        array = next_array
        count += round_count
        if round_count == 0:
            return count


if __name__ == "__main__":
    with open("./input04.txt", "r") as f:
        array = [list(line.rstrip()) for line in f.readlines()]
        print(count_part1(demo))  # 13
        print(count_part1(array)) # 1478
        print(count_part2(demo))  # 43
        print(count_part2(array)) # 9120
