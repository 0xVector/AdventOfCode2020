from collections import deque
with open("inputs/day15.txt") as file:
    data = [line.strip() for line in file]


def play(n):
    for i in range(starting_number_count, n):

        last = numbers[-1]

        if len(number_indices[last]) >= 2:
            last_spoken = number_indices[last][1]
            last_last_spoken = number_indices[last][0]
            new = last_spoken - last_last_spoken
        else:
            new = 0
        numbers.append(new)

        if new not in number_indices:
            number_indices[new] = deque(maxlen=2)

        number_indices[new].append(i)

    return new


# Part 1 ===
numbers = list(map(int, data[0].split(",")))
number_indices = {number: deque([i], maxlen=2) for i, number in enumerate(numbers)}
starting_number_count = len(number_indices)
part1 = play(2020)


# Part 2 ===
numbers = list(map(int, data[0].split(",")))
number_indices = {number: deque([i], maxlen=2) for i, number in enumerate(numbers)}
part2 = play(30000000)


print("Part 1:", part1)
print("Part 2:", part2)
