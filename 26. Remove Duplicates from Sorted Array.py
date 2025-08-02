class Solution(object):  
    def removeDuplicates(self, nums):
        uzunluk = len(nums)
        sayac = 1
        for i in range(uzunluk-1):
            if(nums[i] != nums[i+1]):
                nums[sayac]=nums[i+1]
                sayac +=1
        return sayac
