class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        num = {}
        for i in range(len(nums)):
            s = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    s += 1
            
            num[i] = s
        for k in range(len(nums)):
            nums[k] = num[k]
        
        return nums