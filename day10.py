with open("inputs/day10.txt") as file:
    data = [int(line) for line in file]

# Part 1 ===
diff1 = 0
diff3 = 0

data.insert(0, 0)  # power outlet
device = max(data) + 3
data.append(device)
data.sort()
size = len(data)

for i in range(size):

    if i == size - 1:  # Last
        break

    diff = data[i+1] - data[i]

    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

part1 = diff1 * diff3


# Part 2 ===
results = [1, 0, 0]

for i in range(1, size-1):  # From second element to the second last element

    if data[i] - data[i-1] <= 3:
        num = results[0]

    if i - 2 >= 0:
        if data[i] - data[i-2] <= 3:
            num = sum(results[0:2])

    if i - 3 >= 0:
        if data[i] - data[i-3] <= 3:
            num = sum(results)

    results.insert(0, num)  # Add new result to the beginning
    results.pop()  # Remove the oldest result

part2 = results[-1]  # Take last result


print("Part 1:", part1)
print("Part 2:", part2)
