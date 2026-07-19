class Solution(object):
    def digitFrequencyScore(self, n):
        fre = {}
        while n > 0:
            digit = n%10

            if digit in fre:
                fre[digit] += 1
            else:
                fre[digit] = 1
            
            n//=10
        
        score = 0
        for  digit, fre in fre.items():
            score += digit * fre
        return score