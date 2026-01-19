class Solution(object):
    def transformArray(self, nums):
        even, odd= 0, 0
        for i in range(len(nums)):    
            if nums[i] % 2 == 0:
                even += 1
            else:
                odd += 1

        ct_nums = [0] * even + [1] * odd 
        return ct_nums