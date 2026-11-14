class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        a = float('inf')
        for i in range(len(nums)):
            for j in range(l, r+1):
                if i+j <= len(nums):
                    toplam = sum(nums[i:i+j])
                    if toplam < a and toplam > 0:
                        a = toplam
        
        if a == float('inf'):
            return -1
        return a

        