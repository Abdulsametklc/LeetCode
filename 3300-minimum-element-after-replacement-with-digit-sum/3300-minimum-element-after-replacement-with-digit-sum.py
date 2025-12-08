class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            a = 0
            num = str(nums[i])
            for n in num:
                a += int(n)
            nums[i] = a
        en_kucuk = nums[0]
        for i in range(1,len(nums)):
            if en_kucuk > nums[i]:
                en_kucuk = nums[i]
        return en_kucuk