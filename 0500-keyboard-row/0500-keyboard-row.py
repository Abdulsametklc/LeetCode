class Solution(object):
    def findWords(self, words):
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        
        result = []

        for word in words:
            f_1, s_1, t_1 =0,0,0
            for ch in word.lower():
                if ch in first:
                    f_1 += 1
                elif ch in second:
                    s_1 += 1
                elif ch in third:
                    t_1 += 1
            
            sayi = [f_1, s_1, t_1].count(0)
            if sayi == 2:
                result.append(word)
        return result   