class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc, dec, len_max = 1,1,1
        for i in range(len(nums)-1):  
            if nums[i] < nums[i+1]:
                inc = 1
                dec +=1
                if dec > len_max:
                    len_max = dec
            
            elif nums[i] > nums[i+1]:
                dec = 1
                inc +=1
                if inc > len_max:
                    len_max = inc
            
            else:
                inc, dec = 1,1
        
        return len_max