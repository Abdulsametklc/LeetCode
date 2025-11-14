class Solution(object):
    def selfDividingNumbers(self, left, right):
            dividing = []
            for i in range(left, right+1):
                valid = True
                for d in str(i):
                    if d == '0' or i % int(d) != 0:
                        valid = False
                        break
                if valid:
                    dividing.append(i)
            
            return dividing