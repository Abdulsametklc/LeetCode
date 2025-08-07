class Solution(object):
    def addBinary(self, a, b):
        toplam = int(a,2) + int(b,2) #2'lik tabanda yer alan bir sayıyı integer değerinde onluk tabanında sayıya çevirir.
        sonuc = bin(toplam)[2:] #Stringe çevirir. Çevirme işleminde ilk karakter türü verdiği için bu kısım atılır ve sonraki kısımlar baz alınır.
        return sonuc