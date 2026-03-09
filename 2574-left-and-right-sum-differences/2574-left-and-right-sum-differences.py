class Solution(object):
    def leftRightDifference(self, nums):
        a = len(nums)
        diff = [0] * (a)
        for i in range(a):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            diff[i] = abs(left - right)     
        return diff       