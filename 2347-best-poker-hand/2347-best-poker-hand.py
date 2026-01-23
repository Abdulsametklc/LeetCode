from collections import Counter
class Solution(object):
    def bestHand(self, ranks, suits):
        uzunluk = len(list(set(suits)))
        if uzunluk == 1:
            return "Flush"
        deger = Counter(ranks)
        freq = max(deger.values())
        if freq >= 3:
            return "Three of a Kind"
        elif freq == 2:
            return "Pair"
        else:
            return "High Card"      