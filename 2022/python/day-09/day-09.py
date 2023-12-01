with open('input.txt') as file:
# with open('dummy_input.txt') as file:
    instructions = file.readlines()


# Number of knots - 1 or 9
knots = 1  # later add one to act as the HEAD
knots = 9  # later add one to act as the HEAD

# All segments of the snake
ROPE = [(0, 0)]*(knots+1)
# A list of all visited node coords
visited = [(0,0)]

for instruction in instructions:
    move, count = instruction.strip().split(" ")

    # Dictates the direction we move our x and y coords
    dx = ((move == "R") - (move == "L"))
    dy = ((move == "U") - (move == "D"))

    for c in range(int(count)):
        # Update HEAD's position
        ROPE[0] = (ROPE[0][0]+dx, ROPE[0][1]+dy)

        for segment in range(knots):
            # create our H/T trail as before
            HEAD, TAIL = ROPE[segment], ROPE[segment+1]
            if HEAD == TAIL: continue

            # Relative positions of x and y
            max_dist = max(abs((HEAD[0]-TAIL[0])), abs((HEAD[1]-TAIL[1])))
            if max_dist > 1:

                # These could be done below,
                # but it's easier to see the logic like this
                x, y = TAIL[0], TAIL[1]

                offset = HEAD[0]-TAIL[0]
                if offset != 0:
                    sign = -1 if offset < 0 else 1
                    x += (sign*1)  # 0 or 1
                offset = HEAD[1]-TAIL[1]
                if offset != 0:
                    sign = -1 if offset < 0 else 1
                    y += (sign*1)  # 0 or 1

                T = (x, y)
                ROPE[segment+1] = T
                if segment+1 == knots:
                    visited.append(T)


# Part 1 solution
if knots == 1:
    print(f"Answer to part 1: {len(set(visited))}")
else:
    print(f"Answer to part 2: {len(set(visited))}")
