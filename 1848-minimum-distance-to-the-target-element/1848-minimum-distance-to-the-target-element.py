class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')

        for i in range(len(nums)):
            if target == nums[i]:
                dist = abs(i - start)
                min_dist = min(min_dist, dist)
        
        return min_dist