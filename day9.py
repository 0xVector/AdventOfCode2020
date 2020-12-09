with open("inputs/day9.txt") as file:
    data = [int(line) for line in file]


def check(n):
    for j in preamble:
        if n-j in preamble and n-j != j:
            return False
    return True


# Part 1 ===
numbers = data[25:]
part1 = None
for i in range(len(numbers)):

    preamble = data[i:i+25]

    if check(numbers[i]):
        part1 = numbers[i]
        break


# Part 2 ===
part2, line = None, None
for i in range(len(data)):

    line_sum = 0
    length = 2

    while line_sum < part1:

        line = data[i:i + length]
        line_sum = sum(line)
        length += 1

    if line_sum == part1:
        part2 = min(line) + max(line)
        break


print("Part 1:", part1)
print("Part 2:", part2)
