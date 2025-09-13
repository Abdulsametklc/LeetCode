class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return n
        elif n==1 or n==2:
            return 1
        x,y,z=1,1,0
        for i in range(n-2):
            x,y,z=x+y+z,x,y
        return x