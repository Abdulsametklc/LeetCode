class Solution(object):
    def maxDistance(self, colors):
        a = len(colors)-1
        if colors[0] != colors[a]:
                return a
                
        for i in range(a):
            if colors[0] != colors[a-i]:
                return a-i 
            if colors[a] != colors[i]:
                return a-i  