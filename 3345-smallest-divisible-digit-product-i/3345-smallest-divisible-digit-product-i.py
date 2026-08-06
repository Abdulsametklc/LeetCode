class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            n_str, deger = str(n), 1
            for digit in n_str:
                deger *= int(digit)
            
            if deger % t == 0:
                return n
            else:
                n+= 1