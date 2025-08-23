class Solution(object):
    def majorityElement(self, nums):
        cok = None
        oy = 0

        for i in nums:
            if oy == 0:
                cok = i
                oy = 1

            elif cok == i:
                oy +=1
            
            else:
                oy -=1
                
        return cok