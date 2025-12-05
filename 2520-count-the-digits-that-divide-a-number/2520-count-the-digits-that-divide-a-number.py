class Solution(object):
    def countDigits(self, num):
        num_str, s = str(num), 0
        for a in num_str:
            if num % int(a)==0:
                s +=1
        return s
        