class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        while n > -1:
            n -=i
            i +=1
        return i-2      