class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = []
        num_set = set(nums)
        for i in range(1,len(nums)+1):
            if i not in num_set:
                n.append(i)
        return n