with open("inputs/day21.txt") as file:
    data = [line.strip() for line in file]


# Part 1 ===
allergen_candidates = {}

all_allergens = set()
all_ingredients = set()
allergenic_ingredients = set()

ingredient_lines = []

for line in data:
    line = line.split(" (contains ")
    ingredients = line[0].split()
    allergens = line[1].replace(")", "").replace(",", "").split()

    all_allergens.update(allergens)
    all_ingredients.update(ingredients)

    ingredient_lines.append(ingredients)

    for allergen in allergens:
        if allergen not in allergen_candidates:  # Add all ingredients to potential allergens
            allergen_candidates[allergen] = set(ingredients)

        else:  # Make intersection
            allergen_candidates[allergen].intersection_update(ingredients)

allergen_to_ingredient = {}

while len(allergen_to_ingredient) != len(all_allergens):
    for allergen, ingredients in allergen_candidates.items():

        ingredients -= allergenic_ingredients

        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            allergen_to_ingredient[allergen] = ingredient
            allergenic_ingredients.add(ingredient)

non_allergenic_ingredients = all_ingredients - allergenic_ingredients

part1 = 0
for line in ingredient_lines:
    part1 += len(non_allergenic_ingredients.intersection(line))


# Part 2 ===
sorted_ingredients = []
for allergen, ingredient in sorted(allergen_to_ingredient.items()):
    sorted_ingredients.append(ingredient)
part2 = ",".join(sorted_ingredients)


print("Part 1:", part1)
print("Part 2:", part2)
print(part2 == "cfzdnz,htxsjf,ttbrlvd,bbbl,lmds,cbmjz,cmbcm,dvnbh")
