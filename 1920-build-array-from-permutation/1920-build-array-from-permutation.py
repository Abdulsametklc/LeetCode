class Solution(object):
    def buildArray(self, nums):
        n, i = len(nums), 0
        liste = []
        while n > 0:
            liste.append(nums[nums[i]])
            n -=1
            i +=1
        return liste