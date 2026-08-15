class Solution(object):
    def shiftGrid(self, grid, k):
        grid_1, grid_2 = [], []

        for satir in grid:
            for eleman in satir:
                grid_1.append(eleman)

        k = k % len(grid_1)

        grid_1 = grid_1[-k:] + grid_1[:-k]

        n = len(grid[0])

        for i in range(0, len(grid_1), n):
            grid_2.append(grid_1[i:i+n])

        return grid_2