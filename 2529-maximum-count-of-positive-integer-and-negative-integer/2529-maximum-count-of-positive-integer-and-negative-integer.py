class Solution(object):
    def maximumCount(self, nums):
        n,p = 0,0
        for num in nums:
            if num > 0:
                p += 1
            elif num < 0:
                n += 1
        return max(n,p)       