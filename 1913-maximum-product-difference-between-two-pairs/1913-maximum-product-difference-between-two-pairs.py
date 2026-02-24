class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        a = len(nums)
        return (nums[a-1] * nums[a-2]) - (nums[0] * nums[1])