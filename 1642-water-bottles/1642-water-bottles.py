class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        toplam,n = numBottles, True
        while n:
            if numBottles < numExchange:
                n = False
            kalan = numBottles % numExchange
            numBottles /=numExchange
            toplam += numBottles
            numBottles += kalan
            
        return toplam     