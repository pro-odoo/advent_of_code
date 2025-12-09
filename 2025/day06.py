demo = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.split("\n")

def multiply(operands):
    total = operands[0]
    for i in range(1, len(operands)):
        total *= operands[i]
    return total


def sum_part1(_lines):
    lines = []
    for line in _lines:
        lines.append(
            list(filter(lambda x: x != "", [line.strip() for line in line.split(" ")])))
    total = 0
    for i in range(len(lines[0])):
        operator = lines[-1][i]
        operands = [int(op[i]) for op in lines[:-1]]
        result = 0
        if operator == "*":
            result = multiply(operands)
        else:
            result = sum(operands)
        total += result
    return total

def get_max_len(lines, index):
    return max([len(line[index]) for line in lines])


def compute_operands(operands):
    new_operands = []
    for i in range(len(operands[0])):
        new_number = "".join([op[i] for op in operands])
        new_operands.append(int(new_number))
    return new_operands

def sum_part2(lines):
    tmp = []
    for line in lines:
        tmp.append(
            list(filter(lambda x: x != "", [line.strip() for line in line.split(" ")])))
    # print(tmp)
    lens = [get_max_len(tmp, index) for index in range(len(tmp[0]))]
    numbers = []
    for x in range(len(lines)):
        to_add = []
        for i in range(len(lens)):
            num = lines[x][:lens[i]]
            if x < len(lens):
                lines[x] = lines[x][lens[i] + 1:]
            to_add.append(num)
        numbers.append(to_add)
    total = 0
    _numbers = []
    for i in range(len(numbers[0])):
        calculation = []
        for j in range(len(numbers)):
            calculation.append(numbers[j][i])
        _numbers.append(calculation)
    for calculation in _numbers:
        operands = compute_operands(calculation[:-1])
        operator = calculation[-1].strip()
        result = 0
        if operator == "*":
            result = multiply(operands)
        else:
            result = sum(operands)
        total += result

    return total

if __name__ == "__main__":
    with open("./input06.txt", "r") as f:
        lines = [line for line in f.readlines()]
        print(sum_part1(demo))  # 4277556
        print(sum_part1(lines))  # 4693159084994
        print(sum_part2(demo))  # 3263827
        print(sum_part2(lines))  # 11643736116335
