with open("inputs/day5.txt") as file:
    data = [line.strip() for line in file]

seats = []

# Part 1 ===
for passport in data:

    lower = 0  # F
    upper = 127  # B

    # Row
    for i in range(7):

        mid = (lower + upper) / 2

        if passport[i] == "F":
            upper = int(mid)

        elif passport[i] == "B":
            if not mid.is_integer():
                mid += 1
            lower = int(mid)

    row = lower

    # Col
    lower = 0  # L
    upper = 7  # R

    for i in range(7, 10):

        mid = (lower + upper) / 2

        if passport[i] == "L":
            upper = int(mid)

        elif passport[i] == "R":
            if not mid.is_integer():
                mid += 1
            lower = int(mid)

    col = lower

    seat_id = row * 8 + col

    seats.append(seat_id)


# Part 2 ===
seats.sort()

count = seats[0]
for i in range(len(seats)):
    if count != seats[i]:
        break

    count += 1

print("Part 1:", max(seats))
print("Part 2:", count)
