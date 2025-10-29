class Solution(object):
    def smallestNumber(self, n):
        if n == 0 or n==1:
            return 1
        
        binary = ""

        while n > 0:
            kalan = n%2
            binary = str(kalan) + binary
            n = n//2 

        a = 2**(len(binary))-1
        return a