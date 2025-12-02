class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        n = n**2
        if maxWeight >= n*w:
            return n
        else:
            return maxWeight//w
        