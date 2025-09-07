class Solution(object):
    def hammingWeight(self, n):
        sayac = 0
        while n > 0:
            kalan = n%2
            n = n//2
            if kalan == 1:
                sayac +=1
                kalan = 0
        return sayac
        