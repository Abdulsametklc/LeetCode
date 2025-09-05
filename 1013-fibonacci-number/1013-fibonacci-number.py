class Solution(object):
    def fib(self, n):
        if n==0 or n==1:
            return n
        toplam1=0
        toplam2=1
        toplam3=0
        for i in range(n-1):
            toplam3 = toplam2 + toplam1
            toplam1 = toplam2
            toplam2 = toplam3
        return toplam3

        