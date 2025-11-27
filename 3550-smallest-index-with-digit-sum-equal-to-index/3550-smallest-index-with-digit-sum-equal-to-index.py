class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                if i == nums[i]:
                    return i
            else:
                if i == sum(int(d) for d in str(nums[i])):
                    return i
        return -1