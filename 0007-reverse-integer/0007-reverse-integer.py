class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        r = 0
        while x != 0:
            p = x % 10
            x //= 10

            
            if r > INT_MAX // 10 or (r == INT_MAX // 10 and p > 7):
                return 0

            r = r * 10 + p

        return sign * r
