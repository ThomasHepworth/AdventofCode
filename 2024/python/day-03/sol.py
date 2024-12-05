import re

with open("input.txt") as f:
    # with open("dummy_input.txt") as f:
    instructions = f.read()


def map_mul_string(mul_string: str) -> tuple[int, int]:
    try:
        # return map(int, mul_string.split(","))
        a, b = mul_string.split(",")
        return int(a), int(b)
    except ValueError:
        return 0, 0


def sum_mul_string(instructions: str) -> int:
    mul_finder = re.compile(r"mul\(([^()]*)\)")
    multiples = mul_finder.findall(instructions)
    return sum([a * b for a, b in map(map_mul_string, multiples)])


# Part 1
print(f"Part 1 solution: {sum_mul_string(instructions)}")

# Everything to the left can be processed, right needs to be checked
dontsplit = instructions.split("don't()")

rolling_sum = 0
rolling_sum += sum_mul_string(dontsplit[0])

for dont in dontsplit[1:]:
    do = dont.split("do()")
    rolling_sum += sum([sum_mul_string(d) for d in do[1:]])


print(f"Part 2 solutions: {rolling_sum}")
