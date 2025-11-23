class Solution(object):
    def projectionArea(self, grid):
        xy, yz, zx = 0, 0, 0
        for i in range(len(grid)):
            yz += max(grid[i])
            column_max = 0
            for j in range(len(grid[0])):
                column_max = max(column_max, grid[j][i])
                if grid[i][j] != 0:
                    xy += 1
            zx += column_max
        
        toplam = xy+yz+zx
        return toplam
            
        

        