from itertools import batched

def duplicates_part1(ranges):
    count = 0
    for r in ranges:
        boundaries = r.split("-")
        for i in range(int(boundaries[0]),int(boundaries[1])+1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            mid = len(s)//2
            if s[:mid] == s[mid:]:
                count+=i
    return count

def are_all_parts_equal(parts):
    return all(part == parts[0] for part in parts)

def duplicates_part2(ranges):
    count = 0
    for r in ranges:
        boundaries = r.split("-")
        for i in range(int(boundaries[0]), int(boundaries[1])+1):
            s = str(i)
            for divisors in range(1, len(s)//2+1):
                all_parts = batched(s, divisors)
                if are_all_parts_equal(list(all_parts)):
                    count += i
                    break
    return count

if __name__ == "__main__":
    with open("./input02.txt", "r") as f:
        lines = f.readlines()
        ranges = lines[0].strip().split(",")
        print(duplicates_part1(ranges))  # 21139440284
        print(duplicates_part2(ranges))  # 38731915928
