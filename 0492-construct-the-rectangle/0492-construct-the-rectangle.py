class Solution(object):
    def constructRectangle(self, area):
        kucuk, out = float('inf'), []
        for w in range(1,int(area**0.5)+1):
            if area % w == 0:
                l = area // w
                if l - w < kucuk:
                    kucuk = l - w
                    out = [l,w]       
        return out