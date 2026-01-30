class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        SA = sum(aliceSizes)
        SB = sum(bobSizes)
        diff = (SA - SB) // 2

        bobSet = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bobSet:
                return [a,b]