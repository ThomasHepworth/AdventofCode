from collections import namedtuple


ScanDirection = namedtuple("ScanDirection", ["dx", "dy", "direction"])

up_left = ScanDirection(-1, -1, "Up-left")
up_right = ScanDirection(1, -1, "Up-right")
down_left = ScanDirection(-1, 1, "Down-left")
down_right = ScanDirection(1, 1, "Down-right")

DIRECTIONS = [
    ScanDirection(0, -1, "Up"),
    ScanDirection(0, 1, "Down"),
    ScanDirection(-1, 0, "Left"),
    ScanDirection(1, 0, "Right"),
    up_left,
    up_right,
    down_left,
    down_right,
]

WORD_TO_FIND = "XMAS"

with open("input.txt") as f:
    # with open("dummy_input.txt") as f:
    xmas_fever = [line.strip() for line in f]


def scan(x: int, y: int, direction: ScanDirection, grid: list[str]) -> bool:
    try:
        for i, letter in enumerate(WORD_TO_FIND):
            nx, ny = x + i * direction.dx, y + i * direction.dy
            if nx < 0 or ny < 0:
                return False
            if grid[ny][nx] != letter:
                return False
        return True
    except IndexError:
        # Out of bounds
        return False


def find_xmas(grid: list[str]) -> list[tuple[int, int, str]]:
    matches = []
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter != WORD_TO_FIND[0]:
                continue
            for direction in DIRECTIONS:
                if scan(x, y, direction, grid):
                    matches.append((x, y, direction))
    return matches


def is_in_bounds(x: int, y: int, grid: list[str]) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def check_x_shape(grid: list[str], x: int, y: int) -> bool:
    left_diagonal = [
        ScanDirection(-1, -1, "Up-left"),
        ScanDirection(1, 1, "Down-right"),
    ]
    right_diagonal = [
        ScanDirection(1, -1, "Up-right"),
        ScanDirection(-1, 1, "Down-left"),
    ]

    def collect_diagonal(diagonal):
        try:
            return [
                grid[y + d.dy][x + d.dx]
                for d in diagonal
                if is_in_bounds(x + d.dx, y + d.dy, grid)
            ]
        except IndexError:
            return []

    left_check = collect_diagonal(left_diagonal)
    right_check = collect_diagonal(right_diagonal)

    return (
        "M" in left_check
        and "S" in left_check
        and "M" in right_check
        and "S" in right_check
    )


def find_x_mas(grid: list[str]) -> int:
    matches = 0

    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            # Focus only on cells containing 'A'
            if letter == "A" and check_x_shape(grid, x, y):
                matches += 1

    return matches


## Part 1
results = find_xmas(xmas_fever)
print(f"Answer to part 1: {len(results)}")

## Part 2
results = find_x_mas(xmas_fever)
print(f"Answer to part 2: {results}")
