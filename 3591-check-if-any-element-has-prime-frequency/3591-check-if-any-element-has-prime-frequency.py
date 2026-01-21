import math
class Solution(object):
    def checkPrimeFrequency(self, nums):
        counting = {}
        for num in nums:
            if num in counting:
                counting[num] += 1
            else:
                counting[num] = 1 
        
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            limit = int(math.sqrt(n))
            for i in range(3, limit + 1, 2):
                if n % i == 0:
                    return False
            return True

        for deger in counting.values():
            if is_prime(deger):
                return True
        return False