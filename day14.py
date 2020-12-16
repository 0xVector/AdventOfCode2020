from itertools import product
with open("inputs/day14.txt") as file:
    data = [line.strip().replace("[", " ").replace("]", " ").replace("=", " ") for line in file]

commands = [line.split() for line in data]

# Part 1 ===
part1 = 0
memory = {}

for command in commands:
    if command[0] == "mask":
        mask = command[1][::-1]

    else:
        address = int(command[1])
        value = command[2]

        new_value = list('0'*36 + str(bin(int(value)))[2:])[::-1]

        for i, vals in enumerate(zip(mask, new_value)):

            mask_char = vals[0]

            if mask_char != "X":
                new_value[i] = mask_char

        new_value = "".join(new_value)[::-1]
        memory[address] = new_value

for entry in memory.values():
    part1 += int(entry, 2)


# Part 2 ===
memory.clear()

for command in commands:
    if command[0] == "mask":
        mask = command[1][::-1]

    else:
        address = command[1]
        value = int(command[2])

        new_address = list('0'*36 + str(bin(int(address)))[2:])[::-1]

        for i, vals in enumerate(zip(mask, new_address)):

            mask_char, address_char = vals

            if mask_char != "0":
                new_address[i] = mask_char

        adress_combination = new_address[:]

        for comb in product((1, 0,), repeat=mask.count("X")):
            adress_combination = new_address[:]

            count = 0
            for i, char in enumerate(new_address):
                if char == "X":
                    adress_combination[i] = str(comb[count])
                    count += 1

            adress_combination = int("".join(adress_combination)[::-1], 2)
            memory[adress_combination] = value
            count = 0

part2 = sum(memory.values())


print("Part 1:", part1)
print("Part 2:", part2)
