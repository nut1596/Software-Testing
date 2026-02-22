def gridChallenge(grid):
    # sort each row
    grid = ["".join(sorted(row)) for row in grid]

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows - 1):
        for col in range(cols):
            if grid[row][col] > grid[row + 1][col]:
                return "NO"

    return "YES"
