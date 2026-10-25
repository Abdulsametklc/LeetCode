class Solution(object):
    def areOccurrencesEqual(self, s):
        a = {}

        for b in s:
            if b in a:
                a[b] += 1
            else:
                a[b] = 1
        
        c = len(a)
        for i in range(1, c):
            if list(a.values())[0] == list(a.values())[i]:
                pass
            else:
                return False
        
        return True