class Solution(object):
    def lengthOfLastWord(self, s):
        kelimeler = s.split()
        uzunluk = len(kelimeler)
        son= len(kelimeler[uzunluk-1])
        return son
        
        