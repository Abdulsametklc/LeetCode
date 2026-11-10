class Solution(object):
    def countNegatives(self, grid):
        count = 0
        n = len(grid[0])

        for row in grid:
            for i in range(n):
                if row[i] < 0:
                    count += n - i
                    break
        
        return count