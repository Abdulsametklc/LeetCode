class Solution(object):
    def intersection(self, nums1, nums2):
        nums1,nums2 = list(set(nums1)), list(set(nums2))
        n1,n2,out=len(nums1), len(nums2),[]
        while n1 >= 0:
            for i in range(0,n2):
                if nums1[n1-1] == nums2[i]:
                    out.append(nums2[i])
                    nums2[i] = -1
            n1 -=1
        return out