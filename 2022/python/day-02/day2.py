# # Initialize an empty list to hold the lists of integers
fname = "input.txt"
fname = "input_dummy.txt"

# Hash map to lookup vals
# We could also convert our letters to ints
score_lookup = {
    "A": 0, "B": 1, "C": 2,
    "X": 0, "Y": 1, "Z": 2,
}

part1=0
part2=0
with open(fname, "r") as f:
    for line in f.readlines():
        a,b=[score_lookup[play] for play in line.strip().split(" ")]
        # LHS is our play and RHS is score for W/L/D
        part1+=sum([b+1, ((b-a+1)%3)*3])
        # LHS is our W/L/D score and RHS is our play
        part2+=sum([b*3, ((a+b-1)%3)+1])

# Answers
print(part1)
print(part2)
