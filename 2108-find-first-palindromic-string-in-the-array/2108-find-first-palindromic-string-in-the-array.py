class Solution(object):
    def firstPalindrome(self, words):
        for n in words:
            c = 0
            l = len(n)
            for i in range(len(n)//2):
                if n[i] == n[l - i-1]:
                    c += 1

            if c == l//2:
                return n
        return ""