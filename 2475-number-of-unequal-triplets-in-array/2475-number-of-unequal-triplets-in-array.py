from math import comb
from collections import Counter

class Solution(object):
    def unequalTriplets(self, nums):
        counts = Counter(nums)
        values = list(counts.values())

        result = 0

        for i in range(len(values)):
            for j in range(i+1, len(values)):
                for k in range(j+1, len(values)):
                    result += values[i] * values[j] * values[k]

        return result  