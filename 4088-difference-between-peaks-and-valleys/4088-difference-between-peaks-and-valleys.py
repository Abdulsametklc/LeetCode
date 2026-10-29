class Solution(object):
    def peakValleyDifference(self, nums):
        t=0
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                t += nums[i]

            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                t -= nums[i]
        
        return t