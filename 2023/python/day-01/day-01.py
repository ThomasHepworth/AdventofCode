from typing import Iterable, Iterator
from functools import partial


NAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMS_MAP = {str(num): str(num) for num in range(1, 10)}
NAME_MAP = {name: str(num) for num, name in enumerate(NAMES, 1)}


# Extract the first mapping that's found
# e.g. - "abconetwothree" -> "one" if using NAME_MAP
def find_first_key(text: str, mapping: Iterable[str], backwards=False) -> Iterator[str]:
    for index in range(len(text)):
        w = text[-index-1:] if backwards else text[index:]
        for key in mapping.items():
            if w.startswith(key):
                return key[1]

find_first_key_backwards = partial(find_first_key, backwards=True)

def find_first_and_last(text, mapping):
    first_key = find_first_key(text, mapping)
    last_key = find_first_key_backwards(text, mapping)
    return int(first_key+last_key)


with open ('input.txt') as f:
    part1, part2 = 0, 0
    for line in f.readlines():
        part1+=find_first_and_last(line, NUMS_MAP)
        part2+=find_first_and_last(line, NAME_MAP)


print(part1)
print(part2)

