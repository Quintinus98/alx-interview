#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            vertex = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(vertex)
    return perimeter


# def island_perimeter(grid):
#     """Returns the perimeter of the island described in grid"""
#     if not grid or not grid[0]:
#         return 0
#     perimeter, rows, cols = 0, len(grid), len(grid[0])

#     # Assumption the grid is surrounded by water

#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == 1:
#                 if row == 0 or grid[row - 1][col] == 0:
#                     perimeter += 1
#                 if row >= rows - 1 or grid[row + 1][col] == 0:
#                     perimeter += 1
#                 if col == 0 or grid[row - 1][col] == 0:
#                     perimeter += 1
#                 if col >= cols - 1 or grid[row + 1][col] == 0:
#                     perimeter += 1
#     return perimeter
