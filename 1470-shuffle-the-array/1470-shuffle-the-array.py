class Solution(object):
    def shuffle(self, nums, n):
        nums2 = []
        for i in range(len(nums)/2):
            nums2.append(nums[i])
            nums2.append(nums[i+n])
        return nums2