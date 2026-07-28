import math
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        tek,cift = 1, 2
        tek_toplam, cift_toplam = 0, 0
        for i in range(n):
            tek_toplam += tek 
            tek +=2

            cift_toplam += cift
            cift += 2
        
        return math.gcd(tek_toplam, cift_toplam)