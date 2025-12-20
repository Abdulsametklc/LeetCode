class Solution(object):
    def luckyNumbers(self, matrix):
        satir1 = []
        for i in range(len(matrix)):
            satir = matrix[i][0] 
            for j in range(len(matrix[0])):      
                if satir > matrix[i][j]:
                    satir = matrix[i][j]
            satir1.append(satir)

        kolon1 = []
        for j in range(len(matrix[0])):
            kolon = matrix[0][j]
            for i in range(len(matrix)):
                if matrix[i][j] > kolon:
                    kolon = matrix[i][j]
            kolon1.append(kolon)

        lucky = []
        for x in satir1:
            if x in kolon1:
                lucky.append(x)
        
        return lucky      