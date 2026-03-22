class Solution(object):
    def countPartitions(self, nums):
        n, freq, diff, c = len(nums), {}, 0, 0
        for i in range(n-1):
            diff = sum(nums[i:]) - sum(nums[:i])
            if diff % 2 == 0:
                c += 1
        return c      