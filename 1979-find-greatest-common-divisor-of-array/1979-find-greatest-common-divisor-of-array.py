class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        a = nums[0] 
        b = nums[len(nums)-1]        
        if b % a == 0:
            return a
        c = 0
        for i in range(1,a):
            if b % i == 0 and a % i == 0:
                c = i
        
        return c