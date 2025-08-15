class Solution(object):
    def reverseWords(self, s):
        kelimeler = s.split()
        kelimeler.reverse()
        return " ".join(kelimeler)