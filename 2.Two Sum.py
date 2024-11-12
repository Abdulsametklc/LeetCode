class Solution(object):
    def twoSum(self, nums, target):
        x = len(nums)
        for i in range (x-1,-1,-1):
            for j in range(x-2,-1,-1):
                if i != j:
                    a = nums[i] + nums[j]
                    if target == a:
                        return [i,j]
