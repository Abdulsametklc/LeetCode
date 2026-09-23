class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        l = len(nums)
        s, b, c = nums[0], nums[l-1], []

        for i in range(s,b+1):
            if i in nums:
                pass
            else:
                c.append(i)
            
        return c      