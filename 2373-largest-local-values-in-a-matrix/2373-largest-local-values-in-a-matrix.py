class Solution(object):
    def largestLocal(self, grid):
        local =[]
        n= len(grid)
        
        for i in range(n-2):
            row = []

            for j in range(n-2):
                buyuk = 0

                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if buyuk < grid[x][y]:
                            buyuk = grid[x][y]
                        
                row.append(buyuk)

            local.append(row)
            
        return local