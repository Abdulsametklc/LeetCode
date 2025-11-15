class Solution(object):
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}

        sayac = 0
        
        for n in range(left, right + 1):
            ones = bin(n).count("1")   
            
            if ones in primes:     
                sayac += 1
        
        return sayac