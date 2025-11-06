class Solution(object):
    def intersect(self, nums1, nums2):
        nums3=[]
        for num1 in nums1:
            for i in range(len(nums2)):
                if num1==nums2[i]:
                    nums3.append(num1)
                    nums2.pop(i)
                    break        
        return nums3