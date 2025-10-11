class Solution(object):
    def countBits(self, n):
        count = [0]*(n+1)
        
        for i in range(n+1):
            sayi, toplam = i, 0
            while sayi > 0:
                kalan = sayi%2
                sayi //= 2
                if kalan == 1:
                    toplam +=1
            count[i] = toplam
        return count