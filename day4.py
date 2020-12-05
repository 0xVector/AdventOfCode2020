with open("inputs/day4.txt") as file:
    data = [line.strip() for line in file]

data.append("")  # we need empty after last

REQUIRED_ENTRIES = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

# Parse data into dicts
passports = []
passport = {}

for line in data:
    if line == "":
        passports.append(passport)
        passport = {}

    else:
        fields = line.split()

        for field in fields:
            field = field.split(":")
            passport[field[0]] = field[1]


# Part 1
part1 = 0
for passport in passports:
    if all(val in passport for val in REQUIRED_ENTRIES):
        part1 += 1


# Part 2
part2 = 0
for passport in passports:

    try:
        byr = 2002 >= int(passport["byr"]) >= 1920
        iyr = 2020 >= int(passport["iyr"]) >= 2010
        eyr = 2030 >= int(passport["eyr"]) >= 2020
        ecl = passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        hcl = passport["hcl"][0] == "#" and len(passport["hcl"][1:]) == 6
        pid = len(passport["pid"]) == 9

        # Throw ValueError if not ints
        int(passport["hcl"][1:], 16)
        int(passport["pid"])

        # hgt checks
        unit = passport["hgt"][-2:]
        value = int(passport["hgt"][:-2])
        if unit == "cm":
            hgt = "hgt" in passport and 193 >= value >= 150
        elif unit == "in":
            hgt = "hgt" in passport and 76 >= value >= 59

        if all((byr, iyr, eyr, ecl, hcl, pid)):
            part2 += 1


    except (KeyError, ValueError):
        pass

print("Part 1:", part1)
print("Part 2:", part2)
