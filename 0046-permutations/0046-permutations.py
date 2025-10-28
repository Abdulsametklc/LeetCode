class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        
        per = []
        for i in range(len(nums)):
            secilen = nums[i]
            kalanlar = nums[:i] +nums[i+1:]

            for p in self.permute(kalanlar):
                per.append([secilen]+p)
        
        return per    