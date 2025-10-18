class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        en_buyuk, uzunluk, deger, kids = candies[0], len(candies), extraCandies, []*len(candies)
        for i in range(1,uzunluk):
            if en_buyuk < candies[i]:
                en_buyuk = candies[i]
        
        for i in range(uzunluk):
            gecici = 0
            gecici = deger + candies[i]
            if gecici >= en_buyuk:
                kids.append(True)
            else:
                kids.append(False)
        
        return kids

        