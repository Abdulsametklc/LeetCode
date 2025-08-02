class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        if x ==5:
            return 5
        else:
            x_str = str(x)
            a = len(x_str)
            sum =0
            for i in range(a-1,-1,-1):
                sum += int(x_str[i])
            if x % sum ==0:
                return sum
            else:
                return -1