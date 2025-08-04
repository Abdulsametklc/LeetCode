class Solution(object):
    def strStr(self, haystack, needle):
        uzunluk = len(haystack)
        uzunluk2 = len(needle)
        sayac2 = 0
        if uzunluk2 == 1:
            sayac2 +=1
        if uzunluk == uzunluk2 == 1:
            if haystack[0] == needle[0]:
                return 0
            else:
                return output2
        for i in range(uzunluk-uzunluk2 + 1):
            if haystack[i] == needle[0]:
                sayac = 0
                if sayac2 == 1:
                    return i
                else:
                    for j in range(uzunluk2):
                        if haystack[i+j] == needle[j]:
                            sayac += 1
                        else:
                            break
                    if sayac == uzunluk2:
                        return i
        return -1