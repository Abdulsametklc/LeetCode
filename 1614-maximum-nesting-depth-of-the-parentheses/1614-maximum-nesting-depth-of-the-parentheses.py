class Solution(object):
    def maxDepth(self, s):
        t, m = 0, 0
        for ch in s:
            if ch == "(":
                t += 1
                m = max(m,t)
            elif ch == ")":
                t -= 1
        return m    