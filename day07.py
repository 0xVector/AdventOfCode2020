with open("inputs/day7.txt") as file:
    data = [line.strip().replace(".", "") for line in file]


def check(bag_color):
    for inner_bag in bags[bag_color]:
        if inner_bag[0] in containing_gold or inner_bag[0] == "shiny gold":
            containing_gold.add(bag_color)
            return True
        if check(inner_bag[0]):
            return True


def dig(bag_name, stack, count_):
    global part2

    stack.append(count_)
    prod = 1
    for i in stack:  # TODO REDUCE
        prod *= i
    part2 += prod

    if len(bags[bag_name]) == 0:
        return

    for bag_ in bags[bag_name]:
        dig(bag_[0], stack[:], bag_[1])


#  Parse data into a dict
bags = {}
for line in data:
    line = line.replace(".", "").replace("bags", "").replace("bag", "").strip()
    line = line.split("contain")
    outer__color = line[0].strip()
    inner_colors = line[1].strip()

    bags[outer__color] = []

    for color_entry in inner_colors.split(","):
        if color_entry == "no other":
            continue
        count = int(color_entry.strip()[0])
        color = color_entry.strip()[2:]
        bags[outer__color].append((color, count))


# Part 1 ===
part1 = 0
containing_gold = set()

for bag in bags:
    if check(bag):
        part1 += 1


# Part 2 ===
part2 = 0
dig("shiny gold", [], 1)
part2 -= 1  # TODO FIX


print("Part 1:", part1)
print("Part 2:", part2)
