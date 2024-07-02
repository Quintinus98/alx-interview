#!/usr/bin/python3
"""Island Perimeter"""
# from typing import List


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if not grid or not grid[0]:
        return 0
    perimeter, rows, cols = 0, len(grid), len(grid[0])

    # Assumption the grid is surrounded by water

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if grid[row - 1][col] == 0:
                    perimeter += 1
                if grid[row + 1][col] == 0:
                    perimeter += 1
                if grid[row - 1][col] == 0:
                    perimeter += 1
                if grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter
