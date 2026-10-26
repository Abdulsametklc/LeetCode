class Solution(object):
    def smallestRangeI(self, nums, k):
        if len(nums) == 1:
            return 0
        nums.sort()
        a = nums[len(nums) -1] - nums[0]
        a -= k*2
        if a < 0:
            return 0

        else:
            return a      