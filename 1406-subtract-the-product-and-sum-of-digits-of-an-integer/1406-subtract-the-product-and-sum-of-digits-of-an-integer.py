class Solution(object):
    def subtractProductAndSum(self, n):
        a,c = 1, 0
        for i in range(len(str(n))):
            kalan = n%10
            d = n//10
            a *= kalan
            c += kalan
            n = d
        return a - c 