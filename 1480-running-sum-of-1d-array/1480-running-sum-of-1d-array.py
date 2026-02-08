class Solution(object):
    def runningSum(self, nums):
        toplam = 0
        for i in range(len(nums)):
            toplam += nums[i]
            nums[i] = toplam
        return nums