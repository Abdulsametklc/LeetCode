class Solution(object):
    def averageValue(self, nums):
        toplam,s = 0,0
        for num in nums:
            if num%2 == 0 and num%3 == 0:
                toplam += num
                s += 1
        if toplam == 0:
            return 0
        return toplam/s