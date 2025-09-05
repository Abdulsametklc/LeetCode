class Solution(object):
    def fib(self, n):
        if n==0 or n==1:
            return n
        x,y = 0,1
        for i in range(n):
            x, y = y, x+y 
        return x

'''Farklı öğrendiğim yöntemle
class Solution(object):
    def fib(self,n):
        if n==0 or n==1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)'''