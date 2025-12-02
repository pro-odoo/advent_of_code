def password_part1(lines):
    dial = 50
    count = 0
    for line in lines:
        number = int(line[1:])
        if line[0] == "L":
            tmp = dial - number
            while tmp < 0:
                tmp+=100
            dial = tmp
        else:
            dial = (dial + number) % 100
        if dial == 0:
            count+=1
    return count


def password_part2(lines):
    dial = 50
    count = 0
    for line in lines:
        initial_dial = dial
        diff = 0
        number = int(line[1:])
        if line[0] == "L":
            tmp = dial - number
            while tmp < 0:
                tmp += 100
                diff+=1
            if tmp == 0:
                diff+=1
            if initial_dial == 0:
                diff-=1
            dial = tmp
        else:
            tmp = dial + number
            while tmp >= 100:
                tmp -= 100
                diff+=1
            dial = tmp
        count+=diff
    return count

if __name__ == "__main__":
    with open("./input01.txt", "r") as f:
        lines = f.readlines()
        print(password_part1(lines)) # 1180
        print(password_part2(lines))
