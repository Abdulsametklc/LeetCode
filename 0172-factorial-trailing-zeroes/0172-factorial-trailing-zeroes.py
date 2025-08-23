class Solution(object):
    def trailingZeroes(self, n):
        sayac = 0
        while n >=5:
            n//=5
            sayac += n
        return sayac