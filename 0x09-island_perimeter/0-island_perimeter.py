#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
Determines the perimeter of an island represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list): 2D grid representing the island and water map.
                     0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
