class Solution(object):
    def sumZero(self, n):
        if n%2 == 0:
            n_list = []
        
        if n%2 != 0:
            n_list = [0]

        if n == 1:
            return n_list
        for i in range(1,(n//2)+1):
            n_list.append(i)
            n_list.append(-i)
        
        return n_list