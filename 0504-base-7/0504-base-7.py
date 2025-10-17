class Solution(object):
    def convertToBase7(self, num):
        if num ==0:
            return "0"
        neg = num < 0
        num = abs(num)
        n, toplam=1,0
        while num > 0:
            kalan = num % 7
            num = num // 7
            toplam = toplam + (kalan * n)
            n *=10
        return "-" + str(toplam) if neg else str(toplam)