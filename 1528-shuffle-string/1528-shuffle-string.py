class Solution(object):
    def restoreString(self, s, indices):
        s1 = [""] * len(s)
        for i in range(len(s)):
            hedef = indices[i]
            s1[hedef] = s[i]
        
        s2 = "".join(s1)
        return s2    