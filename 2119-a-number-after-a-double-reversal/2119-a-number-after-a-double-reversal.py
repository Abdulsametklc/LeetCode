class Solution(object):
    def isSameAfterReversals(self, num):
        num_r = int(str(int(str(num)[::-1]))[::-1])
        return True if num_r == num else False   