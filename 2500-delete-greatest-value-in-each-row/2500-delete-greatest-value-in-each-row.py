class Solution(object):
    def deleteGreatestValue(self, grid):
        for i in range(len(grid)):
            grid[i].sort()
        
        answer = 0

        for j in range(len(grid[0]) - 1, -1, -1):
            maximum = 0
            for i in range(len(grid)):
                maximum = max(maximum, grid[i][j])
            
            answer += maximum
        
        return answer