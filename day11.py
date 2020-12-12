from copy import deepcopy
with open("inputs/day11.txt") as file:
    data = [line.strip() for line in file]


def update1():
    global grid

    for row in range(rows):
        for col in range(cols):

            seat = grid[row][col]
            adjacent = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))

            if seat == "L":

                free = True

                for coords in adjacent:
                    row_ = coords[0]
                    col_ = coords[1]

                    if len(grid) > row + row_ >= 0 and len(grid[0]) > col + col_ >= 0:
                        if grid[row + row_][col + col_] == "#":
                            free = False
                            break

                if free:
                    new_grid[row][col] = "#"

            elif seat == "#":
                count = 0

                for coords in adjacent:
                    row_ = coords[0]
                    col_ = coords[1]

                    if rows > row + row_ >= 0 and cols > col + col_ >= 0:
                        if grid[row + row_][col + col_] == "#":
                            count += 1

                if count >= 4:
                    new_grid[row][col] = "L"

    grid = deepcopy(new_grid)


def update2():
    global grid

    for row in range(rows):
        for col in range(cols):

            seat = grid[row][col]
            adjacent = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))

            if seat == "L":

                free = True

                for coords in adjacent:
                    if sees_occupied(row, col, *coords):
                        free = False
                        break

                if free:
                    new_grid[row][col] = "#"

            elif seat == "#":
                count = 0

                for coords in adjacent:
                    if sees_occupied(row, col, *coords):
                        count += 1

                if count >= 5:
                    new_grid[row][col] = "L"

    grid = deepcopy(new_grid)


def occupied_seats():
    total = 0
    for row in grid:
        total += row.count("#")
    return total


def sees_occupied(row, col, delta_row, delta_col):

    while rows > row + delta_row >= 0 and cols > col + delta_col >= 0:

        col += delta_col
        row += delta_row

        if grid[row][col] == "#":
            return True
        elif grid[row][col] == "L":
            return False

    return False


# Part 1 ===
grid = [list(line) for line in data]
new_grid = deepcopy(grid)
rows = len(grid)
cols = len(grid[0])

occupied = -1
occupied_last = -1

while True:

    update1()
    occupied = occupied_seats()

    if occupied == occupied_last:
        part1 = occupied
        break

    occupied_last = occupied

# Part 2 ===
grid = [list(line) for line in data]
new_grid = deepcopy(grid)

occupied = -1
occupied_last = -1

while True:

    update2()
    occupied = occupied_seats()

    if occupied == occupied_last:
        part2 = occupied
        break

    occupied_last = occupied

print("Part 1:", part1)
print("Part 2:", part2)
