class Solution(object):
    def minMoves(self, nums):
        a, toplam = -1, 0
        for num in nums:
            if a < num:
                a = num
        
        nums.remove(a)
        for num in nums:
            toplam += a - num
        return toplam  