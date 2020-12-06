with open("inputs/day1.txt") as file:
    data = [int(line) for line in file]

# Part 1 ===
for i in data:
    for j in data:
        if i == j:
            continue
        if i + j == 2020:
            part1 = i*j
            break

# Bonus one-liner
part1 = max(i*j if i + j == 2020 else 0 for i in data for j in data)


# Part 2 ===
for i in data:
    for j in data:
        if i == j:
            continue
        for k in data:
            if i == k:
                continue
            if i+j+k == 2020:
                part2 = i*j*k
                break

# Bonus one-liner
part2 = max(i*j*k if i + j + k == 2020 else 0 for i in data for j in data for k in data)


print("Part 1:", part1)
print("Part 2:", part2)
