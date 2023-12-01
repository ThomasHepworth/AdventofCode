from functools import reduce
from operator import and_

# # Initialize an empty list to hold the lists of integers
fname = "input.txt"
# fname = "input_dummy.txt"


def convert_letter_to_int(letter):
    # Alternative and clearer return statements
    # ord(letter) - ord('A') + 27
    # ord(letter) - ord('a') + 1
    l = ord(letter)
    return l - 38 if letter.isupper() else l-96


with open(fname, "r") as f:
    backpacks = f.read()

backpacks = backpacks.split("\n")

### SHORTER SOLUTION
# Could also use set intersection...
# Part 1 answer...
part1 = sum([
    convert_letter_to_int(
        reduce(and_, [set(b[:len(b)//2]), set(b[len(b)//2:])]).pop()
    ) for b in backpacks]
)
print(part1)


part2 = sum([
    convert_letter_to_int(
        reduce(and_, map(set, backpacks[n*3:(n+1)*3])).pop()
    ) for n in range(len(backpacks)//3)]
)
print(part2)

