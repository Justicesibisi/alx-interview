#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
    grid (list of list of integers): The 2D grid representing the map of the island.
                                    0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the cell is land
            if grid[i][j] == 1:
                # Check all four sides (up, down, left, right) for water or edge of grid
                if i == 0 or grid[i - 1][j] == 0:  # Top edge or water above
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Bottom edge or water below
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left edge or water to the left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Right edge or water to the right
                    perimeter += 1

    return perimeter
