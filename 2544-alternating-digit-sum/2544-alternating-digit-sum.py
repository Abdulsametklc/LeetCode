class Solution(object):
    def alternateDigitSum(self, n):
        a, toplam, s = len(str(n)), 0, 0
        d = 10 ** (a-1)
        for i in range(a):
            digit = n / d
            n = n - digit * d

            if s%2 == 0:
                toplam += digit

            else:
                toplam -= digit

            s += 1
            d /= 10
            
        return toplam    