with open("inputs/day25.txt") as file:
    data = [line.strip() for line in file]

prime = 20201227
public_key_card = int(data[0])
public_key_door = int(data[1])


def transform(value, subject):
    return (value * subject) % prime


# Part 1 ===
# Crack the card secret key
loop_size = 0
result = 1
while result != public_key_card:
    loop_size += 1
    result = (result * 7) % prime

secret_key_card = loop_size

# Calculate the encryption key
part1 = pow(public_key_door, secret_key_card, prime)


# Part 2 ===
part2 = "Merry Christmas! :-)"


print("Part 1:", part1)
print("Part 2:", part2)
