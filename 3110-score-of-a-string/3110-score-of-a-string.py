class Solution(object):
    def scoreOfString(self, s):
        toplam = 0
        for i in range(len(s)-1):
            toplam += abs(ord(s[i]) - ord(s[i+1])) 
        return toplam