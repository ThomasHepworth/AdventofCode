fname = "input.txt"
# fname = "input_dummy.txt"

with open(fname, "r") as f:
    cleaning_sectors = f.readlines()


[sectors.strip().split(",") for sectors in cleaning_sectors]

part1 = 0
part2 = 0
for sectors in cleaning_sectors:
    a,b = sectors.strip().split(",")
    a_lower, a_upper = [int(a) for a in a.split("-")]
    b_lower, b_upper = [int(b) for b in b.split("-")]

    if a_lower <= b_lower and a_upper >= b_upper:
        part1+=1
    elif b_lower <= a_lower and b_upper >= a_upper:
        part1+=1

    if a_lower <= b_upper and a_upper >= b_lower:
        part2+=1


print(part1)
print(part2)
