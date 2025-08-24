class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        sayac = 0
        k = 0
        for i in range(len(nums)):
            if nums[i]==1:
                sayac +=1
                if sayac > k:
                    k = sayac
            else:
                sayac = 0
        return k     