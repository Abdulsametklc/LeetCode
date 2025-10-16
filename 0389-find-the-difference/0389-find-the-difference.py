from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        
        for ch in count_t:
            if count_t[ch] != count_s.get(ch, 0):
                return ch