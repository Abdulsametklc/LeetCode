class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while num>0:
            if num % 2==1: 
                step +=1
                num -=1
                continue
            num = num/2
            step +=1
        return step    