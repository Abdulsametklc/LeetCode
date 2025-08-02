class Solution(object):
    def minimumOperations(self, nums):
        x = len(nums)
        list = []
        for i in range(x-1,-1,-1):
            if not nums[i] % 3 == 0:
                y = nums[i]
                list.append(y)
        
        z = len(list)
        return z


        