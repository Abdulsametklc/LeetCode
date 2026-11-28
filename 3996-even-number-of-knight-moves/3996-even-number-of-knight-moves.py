class Solution(object):
    def canReach(self, start, target):
        if (start[0] + start[1]) % 2 == 0:
            if (target[0] + target[1]) % 2 == 0:
                return True
            return False
        
        if (start[0] + start[1]) % 2 == 1:
            if (target[0] + target[1]) % 2 == 1:
                return True
            return False