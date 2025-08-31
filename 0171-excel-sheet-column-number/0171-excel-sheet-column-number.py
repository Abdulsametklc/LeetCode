class Solution(object):
    def titleToNumber(self, columnTitle):
        harf_sayi = {}
        toplam = 0
        for i in range(26):
            harf = chr(ord('A') + i)  
            harf_sayi[harf] = i + 1 
        for i in range(len(columnTitle)):
            toplam = (26*toplam) + harf_sayi[columnTitle[i]]
        return toplam