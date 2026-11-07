class Solution(object):
    def countGoodSubstrings(self, s):
        a = 0
        for i in range(len(s)-2):
            sub = s[i:i+3]

            if len(set(sub)) == 3:
                a += 1
        
        return a