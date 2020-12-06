with open("inputs/day2.txt") as file:
    data = [line for line in file]

# Part 1 ===
part1 = 0
for entry in data:

    entry = entry.split()
    numbers = entry[0].split(sep="-")

    minimum = int(numbers[0])
    maximum = int(numbers[1])

    letter = entry[1][0]
    password = entry[2]

    if minimum <= password.count(letter) <= maximum:
        part1 += 1


# Part 2 ===
part2 = 0
for entry in data:

    entry = entry.split()
    numbers = entry[0].split(sep="-")

    pos1 = int(numbers[0])-1
    pos2 = int(numbers[1])-1

    letter = entry[1][0]
    password = entry[2]

    first = password[pos1] == letter
    second = password[pos2] == letter

    # XOR
    if first ^ second:
        part2 += 1

    # Different options:
    # (first and not second) or (second and not first)
    # first != second

print("Part 1:", part1)
print("Part 2:", part2)
