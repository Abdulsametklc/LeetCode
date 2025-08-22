class Solution(object):
    def myPow(self, x, n):
        if n ==0:
            return 1.0

        if n < 0:
            y = 1.0/x
            k = -n
        else:
            y=float(x)
            k = n

        carpim = 1.0

        while k>0:
            if k % 2 ==1:
                carpim *=y
            y *=y
            k //=2
                
        return carpim