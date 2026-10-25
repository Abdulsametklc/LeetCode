class Solution(object):
    def getLucky(self, s, k):
        b = ""

        for a in s:
                b += str(ord(a) - ord("a") + 1) 

        while k > 0:
            d = 0
            for c in b:
                d+= int(c)

            k -=1
            b = str(d) 

        
        return d