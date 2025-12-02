def duplicates_part1(ranges):
    count = 0
    for r in ranges:
        boundaries = r.split("-")
        for i in range(int(boundaries[0]),int(boundaries[1])+1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            mid = int(len(s)/2)
            if s[:mid] == s[mid:]:
                count+=i
    return count


def duplicates_part2(ranges):
    count = 0
    for r in ranges:
        duplicates_ids = set()
        boundaries = r.split("-")
        for i in range(int(boundaries[0]), int(boundaries[1])+1):
            s = str(i)
            for divisors in range(1, int(len(s)/2)+1):
              if len(s) % divisors != 0:
                  continue
              cut = 0
              previous = None
              same = True
              while same and cut < len(s):
                  next_cut = cut + divisors
                  next_one = s[cut:next_cut]
                  if previous != None and previous != next_one:
                      same = False
                  cut = next_cut
                  previous = next_one
              if same:
                  duplicates_ids.add(i)
        count += sum(duplicates_ids)
    return count

if __name__ == "__main__":
    with open("./input02.txt", "r") as f:
        lines = f.readlines()
        ranges = lines[0].strip().split(",")
        print(duplicates_part1(ranges))  # 21139440284
        print(duplicates_part2(ranges))  # 38731915928
