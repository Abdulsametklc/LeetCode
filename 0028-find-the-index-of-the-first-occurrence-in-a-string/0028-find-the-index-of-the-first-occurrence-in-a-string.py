class Solution(object):
    def strStr(self, haystack, needle):
        uzunluk = len(haystack)
        uzunluk2 = len(needle)
        if uzunluk == uzunluk2 == 1:
            if haystack[0] == needle[0]:
                return 0
            else:
                return -1
        for i in range(uzunluk-uzunluk2 + 1):
            if haystack[i] == needle[0]:
                sayac = 0
                for j in range(uzunluk2):
                    if haystack[i+j] == needle[j]:
                        sayac += 1
                    else:
                        break
                if sayac == uzunluk2:
                    return i
        return -1