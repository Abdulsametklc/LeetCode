class Solution(object):
    def maximum69Number (self, num):
        a = len(str(num))-1
        nums = str(num)
        for n in nums:
            if n=='6':
                num += 3*(10**a)
                return num
            a -=1
        return num