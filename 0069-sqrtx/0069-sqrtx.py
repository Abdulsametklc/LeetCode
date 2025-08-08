class Solution(object):
    def mySqrt(self, x):
        # Newton-Raphson yöntemi kullanılmıştır. 
        if x == 0 or x == 1:
            return x

        x0 = x / 2.0  # float bölme
        for i in range(100):
            x0 = (x0 + (x / x0)) / 2.0

        sayi = int(x0)
        # x0 biraz büyük olabilir, bu yüzden düzeltme yap
        if (sayi + 1) * (sayi + 1) <= x:
            return sayi + 1
        elif sayi * sayi > x:
            return sayi - 1
        else:
            return sayi
