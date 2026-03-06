class Solution(object):
    def sumBase(self, n, k):
        if n == 0:
            return 0
            
        result = ""
            
        while n > 0:
            result = str(n % k) + result
            n //= k   

        return sum(int(i) for i in str(result))   