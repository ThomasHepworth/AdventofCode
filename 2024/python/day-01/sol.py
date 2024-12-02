from collections import Counter

with open("input.txt") as f:
    location_ids = [tuple(map(int, line.split())) for line in f]

location_ids_l, location_ids_r = zip(*location_ids)

# Part 1: Calculate the sum of absolute differences
ans_1 = sum(
    abs(right - left)
    for left, right in zip(sorted(location_ids_l), sorted(location_ids_r))
)
print("Part 1:", ans_1)

# Part 2: Calculate the similarity score
rhs_frequency = Counter(location_ids_r)
similarity_score = sum(rhs_frequency[left] * left for left in location_ids_l)
print("Part 2:", similarity_score)
