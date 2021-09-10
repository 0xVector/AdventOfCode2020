with open("inputs/day10.txt") as file:
    data = [int(line) for line in file]

# Part 1 ===
diff1 = 0
diff3 = 0

data.insert(0, 0)  # Power outlet
data.append(max(data) + 3)  # Device
data.sort()
size = len(data)

for i in range(size - 1):
    diff = data[i+1] - data[i]

    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

part1 = diff1 * diff3


# Part 2 ===
count = {0: 1}  # Counts the ways to reach each adapter

for adapter in data[1:]:  # Skip the first adapter (charging outlet - 0)
    # The number of ways to reach is the sum of the number of ways
    # to reach the three previous adapters (those that exist)
    count[adapter] = count.get(adapter-1, 0) + count.get(adapter-2, 0) + count.get(adapter-3, 0)

part2 = count[data[-1]]  # Take the number of ways to reach the device (last adapter)


print("Part 1:", part1)
print("Part 2:", part2)
