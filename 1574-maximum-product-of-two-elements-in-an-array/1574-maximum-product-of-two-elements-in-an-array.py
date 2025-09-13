class Solution(object):
    def maxProduct(self, nums):
        sayac, i = len(nums),0
        en_buyuk,a = nums[0],0
        while sayac > 0:
            if en_buyuk < nums[i]:
                en_buyuk = nums[i]
                a = i
            sayac -=1
            i +=1
        nums.pop(a)
        
        sayac, j = len(nums),0
        en_buyuk2 = nums[0]
        while sayac > 0:
            if en_buyuk2 < nums[j]:
                en_buyuk2 = nums[j]
            sayac -=1
            j +=1

        return (en_buyuk-1)*(en_buyuk2-1)