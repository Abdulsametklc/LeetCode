class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = 0
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        for i in range(m + n):
            for j in range(0, m + n - 1 - i):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]            