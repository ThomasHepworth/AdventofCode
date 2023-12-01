from collections import defaultdict

accelerants = defaultdict(int)

with open("input.txt") as file:
# with open("dummy_input.txt") as file:
    cpu_instructions = file.readlines()

x, cycle = 1, 0
tracker = ""

for instruction in cpu_instructions:
    i = instruction.strip()
    cycle += 1
    # Reset sprite location
    sprite = x%40

    if ((cycle - 20)%40) == 0: accelerants[cycle] = cycle*x
    if cycle % 40 == 0: tracker+="\n"
    # cycle % 40 tells us which pixel is being drawn
    # If this is true, our sprite falls within our CRT
    tracker += "#" if sprite <= (cycle%40) < sprite+3 else "."

    if i != "noop":
        value = int(i.split(" ")[1])
        # Cycles precede CRT moves
        cycle+=1
        tracker += "#" if sprite <= (cycle%40) < sprite+3 else "."
        if ((cycle - 20)%40) == 0: accelerants[cycle] = cycle*x
        if cycle % 40 == 0: tracker+="\n"

        x+=value


print("Answer to part 1:")
print(sum([n for k, n in accelerants.items() if int(k) <= 220]))

print("Answer to part 2:")
print(tracker)
# print("\n".join(
#     [tracker[(n*40):(n*40)+40] for n in range(len(tracker)//40)]
# ))