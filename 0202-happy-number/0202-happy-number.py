class Solution(object):
    def isHappy(self, n):
        def hesapla(sayi):
            toplam = 0
            for digit in str(sayi):
                toplam += int(digit) ** 2
            return toplam
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = hesapla(n)
        
        return n == 1