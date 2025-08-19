class Solution(object):
    def generate(self, numRows):
        pascal = []
        if numRows >= 1:
            pascal.insert(0,[1])

        if numRows >= 2:
            pascal.insert(1,[1,1])
        
        if numRows >2:
            for i in range(2,numRows):
                pascal.append([1])
                for j in range(1,i):
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
                pascal[i].append(1)
        
        return pascal