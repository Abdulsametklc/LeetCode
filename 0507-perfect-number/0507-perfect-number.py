class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        liste = []

        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                d = num // i
                if i != num:
                    liste.append(i)

                if d != i and d != num:
                    liste.append(d)

        toplam = 0
        for i in range(len(liste)):
            toplam += liste[i]

        return toplam == num