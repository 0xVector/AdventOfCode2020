with open("inputs/day1.txt") as file:
    nums = [int(line) for line in file]

# Part 1 ===
for i in nums:
    for j in nums:
        if i == j:
            continue
        if i + j == 2020:
            part1 = i*j
            break


# Part 2 ===
for i in nums:
    for j in nums:
        if i == j:
            continue
        for k in nums:
            if i == k:
                continue
            if i+j+k == 2020:
                part2 = i*j*k
                break

print("Part 1:", part1)
print("Part 2:", part2)
