class Solution(object):
    def destCity(self, paths):
        baslangic = set()
        bitis = set()
        for a, b in paths:
            baslangic.add(a)
            bitis.add(b)
        
        return (bitis - baslangic).pop()