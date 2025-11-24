class Solution(object):
    def prefixesDivBy5(self, nums):
        a, sayi = len(nums), 0
        for i in range(a):
            bit = nums[i]
            
            sayi = sayi*2 + bit

            if sayi%5 == 0:
                nums[i] = True
            else:
                nums[i] = False
        
        return nums