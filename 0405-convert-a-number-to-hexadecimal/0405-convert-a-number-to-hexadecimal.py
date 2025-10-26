class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        if num < 0:
            num = (1 << 32) + num
        
        hex_dig = "0123456789abcdef"
        result =""

        while num > 0:
            remainder = num % 16
            result = hex_dig[remainder] + result
            num //= 16

        return result 
        