class Solution(object):
    def triangularSum(self, nums):
        i,sayac = 0,len(nums)
        if len(nums) == 1:
            return nums[0]
        while sayac > 1:
            for i in range(sayac-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()
            sayac -=1
        return nums[0]
