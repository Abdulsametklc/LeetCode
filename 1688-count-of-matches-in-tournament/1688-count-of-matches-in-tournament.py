class Solution(object):
    def numberOfMatches(self, n):
        mac =  0
        while n != 1:
            if n%2 == 0:
                n = n/2
                mac += n
            else:
                n = n//2
                mac += n
                n += 1
        return mac