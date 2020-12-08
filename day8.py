from copy import deepcopy
with open("inputs/day8.txt") as file:
    data = [line.strip() for line in file]


def check():

    i = 0
    accumulator = 0
    executed = set()

    while True:

        if i == size:
            success = True
            break

        elif i > size or i in executed:
            success = False
            break

        executed.add(i)

        instruction = changed_memory[i][0]
        arg = changed_memory[i][1]

        if instruction == "acc":
            accumulator += arg
            i += 1

        elif instruction == "jmp":
            i += arg

        elif instruction == "nop":
            i += 1

    return success, accumulator


# Parse data
memory = [[line.split()[0], int(line.split()[1])] for line in data]
changed_memory = memory[:]
size = len(memory)


# Part 1 ===
part1 = check()[1]


# Part 2 ===
for i in range(size):

    # Make a deep copy of memory
    changed_memory = deepcopy(memory)
    # We could also just change the original and then revert the changes afterwards (it'd also be faster)
    # but I consider this ... nicer? I can't decide...

    # Change memory
    if changed_memory[i][0] == "jmp":
        changed_memory[i][0] = "nop"

    elif changed_memory[i][0] == "nop":
        changed_memory[i][0] = "jmp"

    else:
        continue

    result = check()
    if result[0]:
        part2 = result[1]
        break


print("Part 1:", part1)
print("Part 2:", part2)
