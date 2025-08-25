class Solution(object):
    def search(self, nums, target):
        if nums[len(nums)/2] > target:
            for i in range(len(nums)/2):
                if nums[i] == target:
                    return i
        
        else:
            for j in range(len(nums)/2,len(nums)):
                if nums[j] == target:
                    return j
        return -1