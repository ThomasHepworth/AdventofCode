import re
from itertools import zip_longest
from collections import deque

fname = "input.txt"

with open(fname, "r") as f:
    puzzle = f.read().split("\n\n")

# Split on the crate number vs array
crate_logs = puzzle[0].split("\n ")[0]
crates = []
for row in [line for line in crate_logs.split("\n")]:
    r = [r for r in re.split(r'\s{4}|\s{1}', row)]
    crates.append(r)

crates[:] = [[x for x in items if x] for items in zip_longest(*crates, fillvalue=None)]
crates_deq = [deque(d) for d in crates]

def pop_n(deq, n):
    return [deq.popleft() for _ in range(n) if len(deq) > 0]

# Parse for threee numbers...
for instruction in puzzle[1].split("\n"):
    # Parse our totals crates to extract, original array and destination array
    extr, orig, desti = [int(s)-1 for s in instruction.split() if s.isdigit()]
    # Then use these to move the crates...
    popped_crates = pop_n(crates_deq[orig], extr+1)
    # Update the part 2 crates...
    # part2_crates[orig] = part1_crates[orig]
    for c in popped_crates:
        crates_deq[desti].appendleft(c)


    popped_crates = crates[orig][:extr+1]
    del crates[orig][:extr+1]
    crates[desti] = popped_crates+crates[desti]

crates
print("".join([c[0].replace("[", "").replace("]", "") for c in crates_deq]))
print("".join([c[0].replace("[", "").replace("]", "") for c in crates]))


#############
# Each row is an instruciton...
a = puzzle[1].split("\n")
extr, orig, desti = [int(s)-1 for s in a[0].split() if s.isdigit()]

for c in pop_n(crates[orig], 2):
    crates[desti].appendleft(c)

crates


move = crates[orig][:extr+1]

crates[desti] = move+crates[desti]

