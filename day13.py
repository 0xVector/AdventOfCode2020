with open("inputs/day13.txt") as file:
    data = [line.strip() for line in file]


def find(ans, bus_value, bus_offset):
    while True:
        if (ans + bus_offset) % bus_value == 0:
            return ans
        ans += increment


# Part 1 ===
depart_time = int(data[0])
buses = [int(number) for number in data[1].split(",") if number != "x"]
best_time = 0

for bus in buses:
    time_to_wait = abs(depart_time - ((depart_time // bus + 1) * bus))

    if time_to_wait < best_time or not best_time:
        best_time = time_to_wait
        best_bus = bus

part1 = best_bus * best_time


# Part 2 ===
buses = [(int(value), offset) for offset, value in enumerate(data[1].split(",")) if value.isnumeric()]
part2 = buses[0][0]
increment = 1

for bus in buses:
    part2 = find(part2, bus[0], bus[1])
    increment *= bus[0]


print("Part 1:", part1)
print("Part 2:", part2)
