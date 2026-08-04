class Solution(object):
    def removeOuterParentheses(self, s):
        s_1 = ""
        sayac = 0

        for ch in s:
            if ch == "(":
                if sayac != 0:
                    s_1 += ch
                sayac += 1
                
            else:
                sayac -=1
                if sayac != 0:
                    s_1 += ch
                      
        return s_1