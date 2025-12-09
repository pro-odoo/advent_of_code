demo = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split("\n")

def merge_ranges(ranges):
    intervals = []
    for r in ranges:
        a, b = map(int, r.split("-"))
        intervals.append((a, b))

    intervals.sort()

    merged = []
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_end:
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))
    return merged

def is_fresh(fresh_ids, ingredient):
    for fresh in fresh_ids:
        if ingredient >= fresh["min"] and ingredient <= fresh["max"]:
            return True
    return False

def count_part1(lines: list):
    index = lines.index("")
    count = 0

    fresh_ids = []
    i = 0
    for line in lines[:index]:
        i+=1
        separator = line.index("-")
        fresh_ids.append({
            "min": int(line[:separator]),
            "max": int(line[separator+1:]),
        })
    for ingredient in lines[index+1:]:
        if is_fresh(fresh_ids, int(ingredient)):
            count+=1
    return count

def count_part2(lines):
    ranges = merge_ranges(lines[:lines.index("")])
    count = 0
    for r in ranges:
        count = count + (r[1] - r[0] + 1)
    return count

if __name__ == "__main__":
    with open("./input05.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        print(count_part1(demo))  # 3
        print(count_part1(lines)) # 868
        print(count_part2(demo))  # 14
        print(count_part2(lines))  # 354143734113772
