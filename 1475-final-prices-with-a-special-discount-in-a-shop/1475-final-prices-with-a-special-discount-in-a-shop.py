class Solution(object):
    def finalPrices(self, prices):
        for i in range(len(prices)):
            if i+1 > len(prices)-1 :
                return prices

            if prices[i] >= prices[i+1]:
                prices[i] = prices[i] - prices[i+1]
            
            else:
                a = i
                while a < len(prices) - 2:
                    a += 1
                    if prices[i] >= prices[a+1]:
                        prices[i] = prices[i] - prices[a+1]
                        break        
        return prices   