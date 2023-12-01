fname = "input.txt"

with open(fname, "r") as f:
    calories = f.read().split("\n\n")

counts = [sum([int(n) for n in c.split("\n")]) for c in calories]
counts.sort()

# Solution 1
print(counts[-1])

# Solution 2
print(sum(counts[-3:]))
