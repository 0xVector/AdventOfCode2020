with open("inputs/day12.txt") as file:
    data = [line.strip() for line in file]

instructions = [(line[0], int(line[1:])) for line in data]

# Part 1 ===
direction = 90  # east
x, y = 0, 0

for instruction in instructions:

    letter = instruction[0]
    value = instruction[1]

    if letter == "N":
        y += value
    elif letter == "S":
        y -= value
    elif letter == "E":
        x += value
    elif letter == "W":
        x -= value

    elif letter == "R":
        direction += value

    elif letter == "L":
        direction -= value

    elif letter == "F":
        if direction == 0:  # north
            y += value
        elif direction == 90:  # east
            x += value
        elif direction == 180:  # south
            y -= value
        elif direction == 270:  # west
            x -= value

    direction %= 360

part1 = abs(x) + abs(y)


# Part 2 ===
x, y = 0, 0
waypoint_x, waypoint_y = 10, 1

for instruction in instructions:

    letter = instruction[0]
    value = instruction[1]

    if letter == "N":
        waypoint_y += value
    elif letter == "S":
        waypoint_y -= value
    elif letter == "E":
        waypoint_x += value
    elif letter == "W":
        waypoint_x -= value

    elif letter == "R":
        for i in range(int(value / 90)):  # switch for each 90° turn
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x

    elif letter == "L":
        for i in range(int(value / 90)):  # switch for each 90° turn
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x

    elif letter == "F":
        x += waypoint_x * value
        y += waypoint_y * value

part2 = abs(x) + abs(y)


print("Part 1:", part1)
print("Part 2:", part2)
