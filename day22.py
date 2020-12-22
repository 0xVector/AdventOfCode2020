from collections import deque
from itertools import islice
with open("inputs/day22.txt") as file:
    data = [line.strip() for line in file]


def recursive_combat(deck1, deck2):
    round_history = set()

    while deck1 and deck2:  # Both not empty

        if (tuple(deck1), tuple(deck2)) in round_history:  # End if you hit a loop
            return 1, deck1

        round_history.add((tuple(deck1), tuple(deck2)))  # Save current game state

        card1, card2 = deck1.popleft(), deck2.popleft()

        # Dive into a sub-game
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner, win_deck = recursive_combat(deque(islice(deck1, 0, card1)), deque(islice(deck2, 0, card2)))

            if winner == 1:
                deck1.extend((card1, card2))
            else:
                deck2.extend((card2, card1))

        # Higher value
        else:
            if card1 > card2:
                deck1.extend((card1, card2))
            else:
                deck2.extend((card2, card1))

    if deck1:
        return 1, deck1
    else:
        return 2, deck2


# Read input data and create decks
deck1_original, deck2_original = deque(), deque()
for line in data:
    if "Player 1" in line:
        deck = deck1_original
    elif "Player 2" in line:
        deck = deck2_original

    if not line.isnumeric():
        continue

    deck.append(int(line))


# Part 1 ===
part1 = 0
deck1, deck2 = deck1_original.copy(), deck2_original.copy()

while deck1 and deck2:  # Both not empty

    card1, card2 = deck1.popleft(), deck2.popleft()

    if card1 > card2:
        deck1.extend((card1, card2))
    else:
        deck2.extend((card2, card1))

if deck1:
    deck = deck1
else:
    deck = deck2

for i, card in enumerate(reversed(deck), start=1):
    part1 += card * i


# Part 2 ===
part2 = 0
deck1, deck2 = deck1_original.copy(), deck2_original.copy()
winner, win_deck = recursive_combat(deck1, deck2)

for i, card in enumerate(reversed(win_deck), start=1):
    part2 += card * i


print("Part 1:", part1)
print("Part 2:", part2)
