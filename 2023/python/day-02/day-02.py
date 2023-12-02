from collections import Counter
import math

MAX_COUNTERS = {"red": 12, "green": 13, "blue": 14}
valid_games = 0  # part 1
product_sums = 0  # part 2

# with open ('dummy_input.txt') as f:
with open ('input.txt') as f:
    for game_id, game in enumerate(f.readlines(), 1):  # games are sequential, so we can use enumerate
        # A counter object to track the largest number of each colour encountered
        game_counter = Counter()
        # Removes 'Game {}:' and pulls out the subgames
        subgames = [game_moves.split(", ") for game_moves in game.strip().split(": ")[1].split("; ")]

        # Clean up our subgames so that each move is in the form -> ("3",  "blue")
        for subgame in subgames:
            moves = (move.split(" ") for move in subgame)
            for number, colour in moves:
                game_counter = game_counter | Counter({colour: int(number)})

        # Part 1
        if all(MAX_COUNTERS[colour] >= game_counter[colour] for colour in MAX_COUNTERS):
            valid_games += game_id
        # Part 2
        product_sums+=math.prod(game_counter.values())


# Solutions
print(f"Solution to part 1: {valid_games}")
print(f"Solution to part 2: {product_sums}")
