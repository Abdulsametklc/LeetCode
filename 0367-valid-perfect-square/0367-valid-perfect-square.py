class Solution(object):
    def isPerfectSquare(self, num):
        num= num**0.5
        return num.is_integer()