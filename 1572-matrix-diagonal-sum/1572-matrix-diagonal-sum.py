class Solution(object):
    def diagonalSum(self, mat):
        a, t = len(mat), 0
        if a == 1:
            return mat[0][0]
        
        for i in range(a):
            t += mat[i][i]
            t += mat[i][a-1-i]
        
        if a%2 == 1:
            t -= mat[a/2][a/2] 
        return t