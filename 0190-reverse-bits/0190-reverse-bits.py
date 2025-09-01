class Solution(object):
    def reverseBits(self, n):
        bits = []

        for _ in range(32):
            bits.append(n & 1)
            n >>=1

        toplam = 0
        for i in range(32):
            toplam += bits[i] * (1<<(31-i))
        return toplam       