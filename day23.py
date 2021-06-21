with open("inputs/day23.txt") as file:
    data = [line.strip() for line in file]

labels = [int(digit) for digit in data[0]]


class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None

    def __repr__(self):
        return "[Cup " + str(self.label) + "] --> " + str(self.next.label)


def generate_labels(count):
    for label in labels:
        yield label
    for i in range(max(labels) + 1, count + 1):
        yield i


def scramble(repeats, count):
    cups = {label: Cup(label) for label in generate_labels(count)}

    last = None
    for label in generate_labels(count):
        if last:
            cups[last].next = cups[label]
        last = label

    current_cup = cups[labels[0]]
    cups[last].next = current_cup

    maximum = max(cups.keys())

    for i in range(repeats):

        first_cup = current_cup.next
        third_cup = current_cup.next.next.next

        # Find the destination label
        destination = current_cup.label
        while destination in {current_cup.label, first_cup.label, current_cup.next.next.label, third_cup.label}:

            destination -= 1
            if destination <= 0:
                destination = maximum

        destination_cup = cups[destination]

        current_cup.next = third_cup.next  # Take 3 cups out

        third_cup.next = destination_cup.next  # Set the 3rd cup taken out to point to cup after dest
        destination_cup.next = first_cup  # Set the destination cup to point to 1st of cups taken out

        current_cup = current_cup.next

    return cups


# Part 1 ===
part1 = ""
scrambled_cups = scramble(100, len(labels))

cup = scrambled_cups[1].next
while len(part1) != len(labels) - 1:
    part1 += str(cup.label)
    cup = cup.next


# Part 2 ===
scrambled_cups = scramble(10**7, 10**6)
part2 = scrambled_cups[1].next.label * scrambled_cups[1].next.next.label


print("Part 1:", part1)
print("Part 2:", part2)
