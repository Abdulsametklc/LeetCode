class Solution(object):
    def totalMoney(self, n):
        a, toplam, d = 1, 0, 0
        for i in range(n):
            toplam += a + d
            d += 1
            if d == 7:
                d = 0
                a += 1  
        return toplam