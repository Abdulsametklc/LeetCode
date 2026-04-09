class Solution(object):
    def minCostToMoveChips(self, position):
        c,t=0,0
        for n in position:
            if n % 2 == 0:
                c += 1
            else:
                t += 1
        return min(c,t)        