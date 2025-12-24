class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity,i,toplam = sorted(capacity, reverse=True),0,sum(apple)
        for b in capacity:
            toplam -= b
            i +=1
            if toplam <= 0:
                return i