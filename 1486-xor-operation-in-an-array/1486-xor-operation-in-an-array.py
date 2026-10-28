class Solution(object):
    def xorOperation(self, n, start):
        t = 0
        for i in range(start, start+(n*2)-1,2):
            t ^= i
        
        return t