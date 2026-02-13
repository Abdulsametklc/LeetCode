import math
class Solution(object):
    def pivotInteger(self, n):
        deger = (n*(n+1))/2
        x = int(sqrt(deger))
        if deger == x*x:
            return x
        else:
            return -1   