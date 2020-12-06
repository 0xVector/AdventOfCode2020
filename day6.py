with open("inputs/day6.txt") as file:
    data = [line.strip() for line in file]

data.append("")

# Parse the data into list of groups
groups, group = [], []

for line in data:
    if line == "":
        groups.append(group)
        group = []

    else:
        group.append(line)


# Part 1 ===
part1 = sum(len(set.union(*map(set, group))) for group in groups)


# Part 2 ===
part2 = sum(len(set.intersection(*map(set, group))) for group in groups)


print("Part 1:", part1)
print("Part 2:", part2)
