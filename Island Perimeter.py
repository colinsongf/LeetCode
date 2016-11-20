class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        row = len(grid)
        if not row:
            return perimeter
        col = len(grid[0])
        if not col:
            return perimeter
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if not i or not grid[i - 1][j]:
                        perimeter += 1
                    if i == row - 1 or not grid[i + 1][j]:
                        perimeter += 1
                    if not j or not grid[i][j - 1]:
                        perimeter += 1
                    if j == col - 1 or not grid[i][j + 1]:
                        perimeter += 1
        return perimeter
