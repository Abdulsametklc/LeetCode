class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        sayac = 0
        sonuc = 0
        for i in range(length-1,-1,-1):
            if val == nums[i]:
                del nums [i]
                sayac += 1
            sonuc = length - sayac      
        return sonuc

        