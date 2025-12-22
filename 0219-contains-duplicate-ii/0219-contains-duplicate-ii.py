class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        contains = {}
        for i in range(len(nums)):
            if nums[i] in contains:
                if i - contains[nums[i]] <= k:
                    return True
            contains[nums[i]] = i
        return False