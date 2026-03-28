class Solution(object):
    def findComplement(self, num):
        num_bin = bin(num)[2:]
        result = ""

        for i in num_bin: 
            if '0' == i:
                result += '1'
            else:
                result += '0'

        return int(result, 2)