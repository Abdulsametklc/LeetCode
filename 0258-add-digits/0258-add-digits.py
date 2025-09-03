class Solution(object):
    def addDigits(self, num): 
        if len(str(num)) == 1:
            return num
        while len(str(num)) > 1:
            toplam = 0
            for digit in str(num):
                toplam += int(digit)
            num = toplam
        return num