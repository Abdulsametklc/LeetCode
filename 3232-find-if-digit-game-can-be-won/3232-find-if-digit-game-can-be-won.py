class Solution(object):
    def canAliceWin(self, nums):
        t1, t2 = 0,0
        for num in nums:
            if 1 == len(str(num)):
                t1 += num
            else:
                t2 += num
        
        return t1!= t2