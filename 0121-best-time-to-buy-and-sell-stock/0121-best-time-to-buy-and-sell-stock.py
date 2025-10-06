class Solution(object):
    def maxProfit(self, prices):
        i=len(prices)
        if i ==1:
            return 0
        kucuk = prices[0]
        sonuc = prices[1] - prices[0]
        for i in range(1,i):
            if prices[i]-kucuk > sonuc:
                sonuc = prices[i]-kucuk
            if kucuk > prices[i]:
                kucuk = prices[i] 
        return 0 if sonuc<0 else sonuc       