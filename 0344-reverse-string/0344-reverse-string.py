class Solution(object):
    def reverseString(self, s):
        deger = len(s)/2
        atama = 0
        for i in range(deger):
            atama = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = atama 