class Solution(object):
    def canAliceWin(self, n):
        c, a = 0, 10
        while n >= a:
            c += 1
            n = n - a
            a -= 1

        if c % 2 == 1:
            return True

        return False       