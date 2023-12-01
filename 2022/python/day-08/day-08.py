# Initialize an empty list to store the numbers
matrix = []

# Open the file and read each line
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(
            [int(l) for l in line.strip()]
        )


def count_viewing_dist(height, trees):
    count = 0
    for tree_hei in trees:
        count += 1
        if height <= tree_hei:
            break

    return count


viewing_dist = 0
invisible_trees = []
# Ignore the first and last rows
for c, row in enumerate(matrix[1:-1]):

    for n, h in enumerate(row):
        # skip outer values
        if n == 0 or n == len(row)-1:
            continue

        # everything to the right
        right = row[n+1:]
        # everything to the left
        left = row[:n]
        # everything above
        # above = above_max[n]
        above = [row[n] for row in matrix[:c+1]]
        # everything below
        below = [row[n] for row in matrix[c+2:]]

        if (
            (h <= max(right)) and
            (h <= max(left)) and
            (h <= max(above)) and
            (h <= max(below))
        ):
            invisible_trees.append(
                (c+1, n)
            )

        # Count viewing dist for tree
        view_dist = (
            count_viewing_dist(h, right)*
            count_viewing_dist(h, below)*
            # reverse above and left
            count_viewing_dist(h, above[::-1])*
            count_viewing_dist(h, left[::-1])
        )

        if viewing_dist < view_dist: viewing_dist = view_dist

# This could be simplified, but logs all of visible trees...
total_trees = len(matrix[0])*len(matrix)
visible_trees = total_trees-len(invisible_trees)
invisible_trees

print("Sol to part 1:")
print(visible_trees)

print("Sol to part 2:")
print(viewing_dist)