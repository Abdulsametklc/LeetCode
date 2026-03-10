class Solution(object):
    def majorityElement(self, nums):
        a = len(nums)
        b, result= {}, []
        for num in nums:
            if num in b:
                b[num] += 1
            
            else:
                b[num] = 1
        
        for key in b:
            if b[key] > a//3:
                result.append(key)
        
        return result       