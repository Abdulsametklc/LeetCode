class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        
        min_a = min(a for a, b in ops)
        min_b = min(b for a, b in ops)
        
        return min_a * min_b
