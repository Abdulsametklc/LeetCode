class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        res = 0
        place = 1
        m = n
        while m > 0:
            bit = m & 1       
            flipped = 1 - bit  
            res += flipped * place
            place <<= 1    
            m >>= 1          
        return res