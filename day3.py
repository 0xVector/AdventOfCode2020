with open("inputs/day3.txt") as file:
    grid = [line[0:-1] for line in file]


def check(right, bottom):

    x, y = 0, 0
    count = 0

    while not y >= len(grid) - 1:

        x += right
        y += bottom

        if x >= width:
            x -= width

        if grid[y][x] == "#":
            count += 1

    return count


width = len(grid[0])

part1 = check(3, 1)
part2 = check(1, 1) * check(3, 1) * check(5, 1) * check(7, 1) * check(1, 2)


print("Part 1:", part1)
print("Part 2:", part2)
