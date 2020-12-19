from re import fullmatch, compile
with open("inputs/day19.txt") as file:
    data = [line.strip() for line in file]


def do(rule_no):

    string = "("
    rule = rules[rule_no].split()

    for value in rule:

        if value.isnumeric():  # Check some other rule
            string += do(value)  # Returns the partial string for that value

        elif value.isalpha():  # A simple letter rule
            string += value  # Just add to our partial string answer

        else:
            string += value

    return string + ")"


messages = []
rule_part = []
message_part = False

for line in data:

    if line == "":
        message_part = True
        continue

    if message_part:
        messages.append(line)
    else:
        rule_part.append(line)

rules = {rule.split(": ")[0]: rule.split(": ")[1].replace('"', "") for rule in rule_part}  # Mozno replace " az neskor?

del message_part, rule_part

# Part 1 ===
part1 = 0

pattern_string = do("0")
pattern = compile(pattern_string)

for message in messages:
    if fullmatch(pattern, message):
        part1 += 1


# Part 2 ===
rules["8"] = "42 +"
#rules["11"] = "42 + 31 +"
# Ugly, but I have no idea how to make it pretty. :-(
rules["11"] = "42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31"
part2 = 0

pattern_string = do("0")
pattern = compile(pattern_string)

pattern8 = do("8")
pattern42 = do("42")
pattern11 = do("11")

for message in messages:
    if fullmatch(pattern, message):
        part2 += 1


print("Part 1:", part1)
print("Part 2:", part2)
