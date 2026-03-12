class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        min_cap, a, c = float('inf'), -1, 0
        for n in capacity:
            if n >= itemSize:
                if n < min_cap:
                    min_cap = n
                    a = c
            c += 1
        
        return a      