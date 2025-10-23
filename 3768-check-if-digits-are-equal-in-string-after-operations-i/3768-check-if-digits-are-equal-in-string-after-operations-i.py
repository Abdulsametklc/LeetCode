class Solution(object):
    def hasSameDigits(self, s):
        s = list(s)
        while len(s) > 2:
            yeni = []
            for i in range(len(s)-1):
                a, b = int(s[i]), int(s[i+1])
                yeniSayi = (a + b) % 10
                yeni.append(str(yeniSayi))
            s = yeni
        return s[0] == s[1]