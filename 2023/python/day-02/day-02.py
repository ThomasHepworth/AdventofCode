from collections import Counter
import math
from functools import reduce

MAX_COUNTERS = {"red": 12, "green": 13, "blue": 14}
valid_games = 0  # part 1
product_sums = 0  # part 2

# with open ('dummy_input.txt') as f:
with open ('input.txt') as f:
    for game_id, game in enumerate(f.readlines(), 1):  # games are sequential, so we can use enumerate
        # Removes 'Game {}:' and pulls out the subgames
        subgames = [game_moves.split(", ") for game_moves in game.strip().split(": ")[1].split("; ")]
        subgames = [(move.split(" ") for move in subgame) for subgame in subgames]
        # Produce a series of Counters
        subgame_counters = [Counter({colour: int(num) for num, colour in subgame}) for subgame in subgames]
        # Counter | Counter -> yields the largest
        game_counter = reduce(lambda x, y: x|y, subgame_counters)
        # Part 1
        if all(MAX_COUNTERS[colour] >= game_counter[colour] for colour in MAX_COUNTERS):
            valid_games += game_id
        # Part 2
        product_sums+=math.prod(game_counter.values())


# Solutions
print(f"Solution to part 1: {valid_games}")
print(f"Solution to part 2: {product_sums}")
