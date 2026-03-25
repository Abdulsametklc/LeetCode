class Solution(object):
    def decompressRLElist(self, nums):
        n = []
        for i in range(0,len(nums),2):
            n.extend([nums[i+1]] * nums[i])
        return n