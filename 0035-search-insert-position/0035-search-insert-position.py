class Solution(object):
    def searchInsert(self, nums, target):
        uzunluk = len(nums)
        for i in range(uzunluk):
            if target == nums[i]:
                return i

        for j in range(uzunluk):
            if target < nums[0]:
                nums.insert(0,target)
                return 0

            elif target > nums[j]:
                if j + 1 < uzunluk and target < nums[j+1]:
                    nums.insert(j+1,target)
                    return j+1 

                elif j + 1 == uzunluk:
                    nums.append(target)
                    return len(nums) - 1      