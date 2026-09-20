class Solution(object):
    def reverseDegree(self, s):
        toplam, carp = 0, 1
        for n in s:
            toplam +=  carp *(26 - ord(n) + ord('a'))
            carp += 1
        
        return toplam