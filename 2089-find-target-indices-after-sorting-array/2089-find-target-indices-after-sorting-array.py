class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        l, nums1 = len(nums), []
        for i in range(l):
            if nums[i] == target:
                nums1.append(i)
        
        return nums1