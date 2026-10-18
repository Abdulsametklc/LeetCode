class Solution(object):
    def countKeyChanges(self, s):
        s = s.lower()
        n, t = len(s), 0
        for i in range(n-1):
            if s[i] != s[i+1]:
                t+=1
        return t