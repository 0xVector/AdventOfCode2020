with open("inputs/day16.txt") as file:
    data = [line.strip() for line in file]

fields = {}
tickets = []
line_breaks = 0

for line in data:

    if line == "":
        line_breaks += 1
        continue

    if line_breaks == 0:  # Fields part
        line = line.split(":")
        intervals = line[1].strip().split(" or ")
        intervals = (tuple(map(int, intervals[0].split("-"))), tuple(map(int, intervals[1].split("-"))))
        fields[line[0]] = intervals

    elif line_breaks == 1:  # My ticket part
        if "your ticket" in line:
            continue

        my_ticket = tuple(map(int, line.split(",")))

    elif line_breaks == 2:  # Nearby tickets part
        if "nearby tickets" in line:
            continue

        tickets.append(tuple(map(int, line.split(","))))

ticket_size = len(fields)


# Part 1 ===
part1 = 0
invalid_tickets = set()

for ticket in tickets:
    for value in ticket:

        found = False

        for field in fields.values():

            first = field[0][0] <= value <= field[0][1]
            second = field[1][0] <= value <= field[1][1]

            if first or second:
                found = True
                break

        if not found:
            invalid_tickets.add(ticket)
            part1 += value


# Part 2 ===
tickets = [ticket for ticket in tickets if ticket not in invalid_tickets]  # Filter out invalid tickets
fields_candidate_positions = {field: set() for field in fields}  # Candidate positions for each field
tickets.append(my_ticket)  # Add my ticket to the batch

for i in range(ticket_size):  # Check each position of ticket values

    values_on_position = [ticket[i] for ticket in tickets]  #

    # Check each field
    for field in fields.items():

        fits = True

        field_name = field[0]
        field_intervals = field[1]

        # Check if all values fit
        for value in values_on_position:
            first = field_intervals[0][0] <= value <= field_intervals[0][1]
            second = field_intervals[1][0] <= value <= field_intervals[1][1]

            if not (first or second):
                fits = False
                break

        if fits:
            fields_candidate_positions[field_name].add(i)

field_to_position = {}
removed = set()

for i in range(ticket_size):  # For each ticket position
    for field_name, candidates in fields_candidate_positions.items():

        candidates -= removed

        if len(candidates) == 1:  # Just one candidate - this position has no dispute and has to be assigned to them
            selected_position = candidates.pop()
            field_to_position[field_name] = selected_position
            removed.add(selected_position)  # We want to remove this position from all other fields - already assigned
            break

part2 = 1
for field_name in field_to_position:  # Calculate product of all departure fields
    if field_name.startswith("departure"):
        part2 *= my_ticket[field_to_position[field_name]]


print("Part 1:", part1)
print("Part 2:", part2)
