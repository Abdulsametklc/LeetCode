class Solution(object):
    def maximumProduct(self, nums):
        a = len(nums)
        nums.sort()

        buyuk = nums[-1]

        sol = nums[0] * nums[1] * buyuk
        sag = nums[-1] * nums[-2] * nums[-3]
        return max(sol,sag)