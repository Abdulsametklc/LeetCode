class Solution(object):
    def countAsterisks(self, s):
        a, side, c = len(s), False, 0
        for b in s:
            if '|' == b:
                side = not side
            if side == False and b == '*':
                c += 1
        
        return c