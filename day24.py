with open("inputs/day24.txt") as file:
    data = [line.strip() for line in file]

paths = [line.replace("nw", "0").replace("sw", "2").replace("se", "3").replace("ne", "5")
             .replace("w", "1").replace("e", "4") for line in data]

MOVES = ((1, -1), (2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1))
SIZE = 215  # Adjust to speed things up. Too low and you get an IndexError.   Part 1: min 60   Part 2: min 215


# Part 1 ===
tiles = [["W" for j in range(SIZE)] for i in range(SIZE)]
middle = (SIZE//2, SIZE//2)

for path in paths:

    new_coord = middle

    for move in path:
        new_coord = tuple(sum(pair) for pair in zip(new_coord, MOVES[int(move)]))

    tile = tiles[new_coord[1]][new_coord[0]]

    if tile == "W":
        tiles[new_coord[1]][new_coord[0]] = "B"

    else:
        tiles[new_coord[1]][new_coord[0]] = "W"

part1 = 0
for row in tiles:
    part1 += row.count("B")


# Part 2 ===
for i in range(100):

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):

            neighbours = 0
            for move in MOVES:  # Count black neighbours
                if y + move[1] < SIZE and x + move[0] < SIZE:  # Border check
                    if tiles[y + move[1]][x + move[0]] in {"B", "V"}:  # Black or formerly black
                        neighbours += 1

            if tile == "B":  # Black tile flip conditions
                if neighbours == 0 or neighbours > 2:
                    tiles[y][x] = "V"  # Wannabe white, will change later

            elif tile == "W":  # White tile flip conditions
                if neighbours == 2:
                    tiles[y][x] = "P"  # Wannabe black, will change later

    for y, row in enumerate(tiles):  # Finish tile flipping
        for x, tile in enumerate(row):

            if tile == "P":
                tiles[y][x] = "B"

            elif tile == "V":
                tiles[y][x] = "W"

part2 = 0
for row in tiles:
    part2 += row.count("B")


print("Part 1:", part1)
print("Part 2:", part2)
