class Solution(object):
    def sumOfUnique(self, nums):
        nums2 = {}
        nums3 = list(set(nums))
        toplam = 0
        for num in nums:
            if num in nums2:
                nums2[num] += 1
            else:
                nums2[num] = 1
        
        for num in nums3:
            if nums2[num] == 1:
                toplam += num
        
        return toplam