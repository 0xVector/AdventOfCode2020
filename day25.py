with open("inputs/day25.txt") as file:
    data = [line.strip() for line in file]

public_key_card = int(data[0])
public_key_door = int(data[1])


def transform(value, subject):
    return (value * subject) % 20201227


# Part 1 ===
# Crack the card secret key
loop_size = 0
result = 1
while result != public_key_card:
    loop_size += 1
    result = transform(result, 7)

secret_key_card = loop_size

# Calculate the encryption key
result = 1
for i in range(secret_key_card):
    result = transform(result, public_key_door)

part1 = result


# Part 2 ===
part2 = "Merry Christmas! :-)"


print("Part 1:", part1)
print("Part 2:", part2)
