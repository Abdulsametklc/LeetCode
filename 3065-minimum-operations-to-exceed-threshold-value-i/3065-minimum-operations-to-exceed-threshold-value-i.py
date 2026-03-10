class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        for num in nums:
            if k > num:
                count += 1
        return count      