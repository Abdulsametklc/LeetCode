class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n%2==0:
            for i in range (1,+32,+1):
                if 2**i==n:
                    return True         
        return False