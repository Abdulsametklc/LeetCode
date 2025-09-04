class Solution(object):
    def missingNumber(self, nums):
        deger = 0
        en_buyuk = nums[0]
        for i in range(1,len(nums)):
            if en_buyuk < nums[i]:
                en_buyuk = nums[i]

        present = [False]*(en_buyuk + 1)

        for num in nums:
            present[num] = True
        
        missing = []
        for i, exists in enumerate(present):
            if not exists:
                return i
            
        return en_buyuk+1