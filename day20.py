from math import sqrt
import numpy as np
with open("inputs/day20.txt") as file:
#with open("inputs/tests/test20.txt") as file:
    data = [line.strip() for line in file]


def from_connections(tile_id):
    return [t[0] for t in connections[tile_id]]


tiles = {}

for line in data:

    if line == "":
        continue

    if "Tile" in line:
        tile_id = int(line.replace(":", "").split()[1])
        tiles[tile_id] = []
        continue

    tiles[tile_id].append(line)


# Part 1 ===
part1 = 0
grid_size = int(sqrt(len(tiles))) * len(data[1])
tile_count = int(sqrt(len(tiles)))
tile_size = len(data[1])
edges = {}

for tile_id, tile in tiles.items():

    for i in range(2):
        for j in range(4):

            if j == 0:  # Top
                edge = tile[0]
            elif j == 1:  # Right
                edge = "".join((i[-1] for i in tile))
            elif j == 2:  # Bottom
                edge = tile[-1]
            elif j == 3:  # Left
                edge = "".join((i[0] for i in tile))

            if i == 1:
                edge = edge[::-1]

            if edge not in edges:
                edges[edge] = []

            edges[edge].append((tile_id, j, i == 1))

single_edges_by_tile = {tile: 0 for tile in tiles}

for properties in edges.values():
    if len(properties) == 1:
        single_edges_by_tile[properties[0][0]] += 1

part1 = 1

for tile_id, value in single_edges_by_tile.items():
    if value == 4:
        corner = tile_id
        part1 *= tile_id

# Part 2 ===
part2 = 0
connections = {tile: [] for tile in tiles}
done_edges = set()

for edge, properties in edges.items():

    if edge[::-1] in done_edges:
        continue

    if len(properties) == 2:  # Valid connection

        tile_id1, tile_id2 = properties[0][0], properties[1][0]
        rotation1, rotation2 = properties[0][1], properties[1][1]
        flipped1, flipped2 = properties[0][2], properties[1][2]

        connections[tile_id1].append((tile_id2, rotation1, flipped1))
        connections[tile_id2].append((tile_id1, rotation2, flipped2))

    done_edges.add(edge)

grid = [["x" for i in range(grid_size)] for j in range(grid_size)]

corner_tile = np.array([list(line) for line in tiles[corner]])
neghbours = from_connections(corner)
used = {corner}
used.update(neghbours)

for flip in range(2):
    for rot in range(4):

        edge_right = [line[-1] for line in corner_tile]
        edge_bottom = list(corner_tile[-1])
        neigh1, neigh2 = False, False

        for tile_id, tile in tiles.items():
            if tile_id == corner:
                continue
            next_tile1 = np.array([list(line) for line in tile])

            for flip2 in range(2):
                for rot2 in range(4):
                    next_edge_left = [line[0] for line in next_tile1]

                    if next_edge_left == edge_right:
                        neigh1 = True
                        break
                    next_tile1 = np.rot90(next_tile1)
                if neigh1:
                    break
                next_tile1 = np.fliplr(next_tile1)
            if neigh1:
                break

        for tile_id, tile in tiles.items():
            if tile_id == corner:
                continue
            next_tile2 = np.array([list(line) for line in tile])

            for flip2 in range(2):
                for rot2 in range(4):
                    next_edge_top = list(next_tile2[0])

                    if next_edge_top == edge_bottom:
                        neigh2 = True
                        break
                    next_tile2 = np.rot90(next_tile2)
                if neigh2:
                    break
                next_tile2 = np.fliplr(next_tile2)
            if neigh2:
                break

        if neigh1 and neigh2:
            for row in range(tile_size):
                for col in range(tile_size):
                    grid[row][col] = corner_tile[row][col]
                    grid[row][col + tile_size] = next_tile1[row][col]
                    grid[row + tile_size][col] = next_tile2[row][col]

        corner_tile = np.rot90(corner_tile)
    corner_tile = np.fliplr(corner_tile)


# Okej, prve mame. podme dalej
start = 2

for i in range(0, grid_size, tile_size): #pre kazdy riadok

    if i != 0:
        start = 1

    # ROW
    for j in range(start*tile_size, grid_size, tile_size):  # Zvysok prveho  st;lpce

        done = False
        edge = [line[j-1] for line in grid[i:i+tile_size]]
        for tile_id, tile in tiles.items():

            if tile_id in used:
                continue

            tile = np.array([list(line) for line in tile])

            for flip in range(2):
                for rot in range(4):

                    next_edge = [line[0] for line in tile]

                    if next_edge == edge:
                        done = True
                        break
                    tile = np.rot90(tile)
                if done:
                    break
                tile = np.fliplr(tile)

            if done:
                for row in range(tile_size):
                    for col in range(tile_size):
                        grid[i+row][j+col] = tile[row][col]
                used.add(tile_id)
                break

    # START NEW ROW, 1 PIECE ONLY
    if i == 0:  # FIRST
        continue

    done = False
    edge = grid[i+tile_size-1][0:tile_size]
    for tile_id, tile in tiles.items():

        if tile_id in used:
            continue

        tile = np.array([list(line) for line in tile])

        for flip in range(2):
            for rot in range(4):

                next_edge = list(tile[0])

                if next_edge == edge:
                    done = True
                    break
                tile = np.rot90(tile)
            if done:
                break
            tile = np.fliplr(tile)

        if done:
            for row in range(tile_size):
                for col in range(tile_size):
                    grid[i + tile_size + row][col] = tile[row][col]
            used.add(tile_id)
            break


# Tak krok 2 mame tiez, teraz vyhadzat bordery...
#clean_grid = [["x" for i in range((tile_size-2)*tile_count)] for j in range((tile_size-2)*tile_count)]
#clean_grid = [[] for i in range((tile_size-2)*tile_count)]
clean_grid = [[]]

for row in range(grid_size):

    if row % tile_size == 0 or (row + 1) % tile_size == 0:
        continue

    for col in range(grid_size):

        if col % tile_size == 0 or (col + 1) % tile_size == 0:
            continue

        clean_grid[-1].append(grid[row][col])

    if row + 2 != grid_size and len(clean_grid[-1]) == (tile_size - 2) * tile_count:
        clean_grid.append([])


# Aj bordery mame vyhadzane, cas ulovit priseru!

monster = [
    list("                  # "),
    list("#    ##    ##    ###"),
    list(" #  #  #  #  #  #   ")
]

found_correct_rotation = False
monsters = 0

# Check all monster rotations
for rot in range(2):
    for flip in range(4):

        # Check all monster positions on map
        for row in range(0, len(clean_grid)-2):
            for col in range(0, len(clean_grid)-19):

                found_problem = False

                # Try monster on this position
                for monster_row in range(3):
                    for monster_col in range(20):

                        if monster[monster_row][monster_col] == "#":
                            if clean_grid[row + monster_row][col + monster_col] != "#":
                                found_problem = True

                # Checked all positions
                if not found_problem:
                    found_correct_rotation = True
                    monsters += 1

        if found_correct_rotation:
            break
        clean_grid = np.rot90(clean_grid)

    if found_correct_rotation:
        break
    clean_grid = np.fliplr(clean_grid)


# Este najdi total #
total = 0
for row in clean_grid:
    total += list(row).count("#")

part2 = total - monsters*15


#for line in clean_grid:
#    print(*line, sep="")

print(monsters)


print("Part 1:", part1)
print("Part 2:", part2)
