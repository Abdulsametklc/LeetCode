class Solution(object):
    def findFinalValue(self, nums, original):
        while True:
            n = 0
            for num in nums:
                if original == num:
                    original = 2 * original
                    n = 1
                    break
            if n==0:
                return original       