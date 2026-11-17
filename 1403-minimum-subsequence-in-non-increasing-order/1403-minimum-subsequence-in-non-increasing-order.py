class Solution(object):
    def minSubsequence(self, nums):
        toplam, sub = sum(nums), []
        nums.sort(reverse=True)
        
        for i in range(len(nums)):
            sub.append(nums[i])
            toplam -= nums[i]
            sub_toplam = sum(sub)
            if sub_toplam > toplam:
                return sub       