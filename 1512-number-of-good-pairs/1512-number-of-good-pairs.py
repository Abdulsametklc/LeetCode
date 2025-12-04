class Solution(object):
    def numIdenticalPairs(self, nums):
        b=0
        nums_1 = set(nums)
        for num in nums_1:
            s,a = 0,0
            for j in range(len(nums)):
                if num == nums[j]:
                    s +=1
            a = (s*(s-1))/2
            b += a
        return b    