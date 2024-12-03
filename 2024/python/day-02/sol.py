with open("input.txt") as f:
    reactor_readings = [[int(value) for value in line.strip().split()] for line in f]


def is_increment_decrement_consistent(diff: int, prev_diff: int) -> bool:
    # This will ignore the first iteration where prev_diff is always 0
    if prev_diff == 0:
        return True
    return diff * prev_diff > 0


def is_valid_reading(reading: list[int], removal_allowed: bool = True) -> bool:
    prev_diff = 0
    print(reading)
    for i in range(len(reading) - 1):
        diff = reading[i + 1] - reading[i]

        if (
            abs(diff) > 3
            or abs(diff) < 1
            or not is_increment_decrement_consistent(diff, prev_diff)
        ):
            if not removal_allowed:
                return False

            print(f"Iteration: {i}")
            return any(
                [
                    is_valid_reading(reading[: i - 1] + reading[i:], False),
                    is_valid_reading(reading[:i] + reading[i + 1 :], False),
                    is_valid_reading(reading[: i + 1] + reading[i + 2 :], False),
                ]
            )
        prev_diff = diff
    return True


# Part 1: Removal allowed (can remove one element)
part1 = sum(
    is_valid_reading(reading, removal_allowed=False) for reading in reactor_readings
)

# Part 2: No removal allowed
part2 = sum(
    is_valid_reading(reading, removal_allowed=True) for reading in reactor_readings
)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
