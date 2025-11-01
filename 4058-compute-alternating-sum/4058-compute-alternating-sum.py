class Solution(object):
    def alternatingSum(self, nums):
        toplam = 0
        for i in range(len(nums)):
            if i%2 ==0:
                toplam += nums[i]
            else:
                toplam -= nums[i]
        return toplam