class Solution(object):
    def createTargetArray(self, nums, index):
        n,i = len(nums),0
        target = []
        while n > 0:
            target.insert(index[i], nums[i])
            i +=1
            n -=1 
        return target      