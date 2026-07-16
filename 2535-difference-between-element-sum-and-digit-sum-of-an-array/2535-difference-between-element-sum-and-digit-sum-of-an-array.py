class Solution(object):
    def differenceOfSum(self, nums):
        a, rakam=0,0
        for n in nums:
            a += n
        
        for u in nums:
            c = self.numeric(u)
            rakam += c

        return abs(a - rakam)

    def numeric(self, j):
        c, toplam=0, 0
        while j > 0:
            c=j%10
            toplam += c
            j=j//10
        return toplam