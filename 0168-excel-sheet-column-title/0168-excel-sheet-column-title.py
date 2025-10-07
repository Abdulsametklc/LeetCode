class Solution(object):
    def convertToTitle(self, columnNumber):
        res = []
        n = columnNumber
        while n > 0:
            n -=1
            rem = n%26
            res.append(chr(ord('A')+rem))
            n //=26
        return ''.join(reversed(res))
        