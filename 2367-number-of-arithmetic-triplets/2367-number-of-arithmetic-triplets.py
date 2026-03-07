class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        s = set(nums)
        count = 0

        for num in nums:
            if num + diff in s and num + 2*diff in s:
                count += 1
        
        return count