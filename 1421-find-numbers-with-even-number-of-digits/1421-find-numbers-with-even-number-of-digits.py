class Solution(object):
    def findNumbers(self, nums):
        sayac, i, j = len(nums), 0, 0
        while sayac > 0:
            n = len(str(nums[i]))
            if n%2 ==0:
                j +=1
            sayac -=1
            i+=1
        return j