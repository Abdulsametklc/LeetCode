class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        
        while k > 0:
            i = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    i = j
            
            nums[i] *= multiplier
            k -= 1
        return nums