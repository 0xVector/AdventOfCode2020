with open("inputs/day17.txt") as file:
    data = [line.strip() for line in file]

# Slooow and horribly ugly solution. Will try to improve later.


def neighbours_active3D(x, y, z):

    active = 0
    for x_ in range(x-1, x+2):
        for y_ in range(y-1, y+2):
            for z_ in range(z-1, z+2):
                if any((x_ >= X, y_ >= Y, z_ >= Z, x_ < 0, y_ < 0, z_ < 0, (x_ == x and y_ == y and z_ == z))):
                    continue

                if plane[z_][y_][x_] in {"#", "I"}:
                    active += 1
    return active


def neighbours_active4D(x, y, z, w):

    active = 0
    for x_ in range(x-1, x+2):
        for y_ in range(y-1, y+2):
            for z_ in range(z-1, z+2):
                for w_ in range(w-1, w+2):
                    if any((x_ >= X, y_ >= Y, z_ >= Z, w_ >= W, x_ < 0, y_ < 0, z_ < 0, w_ < 0, (x_ == x and y_ == y and z_ == z and w_ == w))):
                        continue

                    if plane[w_][z_][y_][x_] in {"#", "I"}:
                        active += 1
    return active


# Part 1 ===
X, Y, Z = 26, 26, 15
plane = [[["." for k in range(X)] for j in range(Y)] for i in range(Z)]
middle = ((X-1)//2, (Y-1)//2, (Z-1)//2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            plane[middle[2]][y+middle[1]][x+middle[0]] = data[y][x]

for cycle in range(6):

    for z in range(Z):
        for y in range(Y):
            for x in range(X):

                if plane[z][y][x] in {"#", "I"}:  # Also consider changed in this cycle, because they all look at the same time
                    if not (neighbours_active3D(x, y, z) in (2, 3)):
                        plane[z][y][x] = "I"

                elif plane[z][y][x] in {".", "A"}:
                    if neighbours_active3D(x, y, z) == 3:
                        plane[z][y][x] = "A"

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if plane[z][y][x] == "I":
                    plane[z][y][x] = "."
                elif plane[z][y][x] == "A":
                    plane[z][y][x] = "#"

part1 = 0
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if plane[z][y][x] == "#":
                part1 += 1


# Part 2 ===
X, Y, Z, W = 26, 26, 15, 15
plane = [[[["." for l in range(X)] for k in range(Y)] for j in range(Z)] for i in range(W)]
middle = ((X-1)//2, (Y-1)//2, (Z-1)//2, (W-1)//2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            plane[middle[3]][middle[2]][y+middle[1]][x+middle[0]] = data[y][x]

for cycle in range(6):

    for w in range(W):
        for z in range(Z):
            for y in range(Y):
                for x in range(X):

                    if plane[w][z][y][x] in {"#", "I"}:  # Also consider changed in this cycle, because they all look at the same time
                        if not (neighbours_active4D(x, y, z, w) in (2, 3)):
                            plane[w][z][y][x] = "I"

                    elif plane[w][z][y][x] in {".", "A"}:
                        if neighbours_active4D(x, y, z, w) == 3:
                            plane[w][z][y][x] = "A"

    for w in range(W):
        for z in range(Z):
            for y in range(Y):
                for x in range(X):
                    if plane[w][z][y][x] == "I":
                        plane[w][z][y][x] = "."
                    elif plane[w][z][y][x] == "A":
                        plane[w][z][y][x] = "#"

part2 = 0
for w in range(W):
    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if plane[w][z][y][x] == "#":
                    part2 += 1


print("Part 1:", part1)
print("Part 2:", part2)
