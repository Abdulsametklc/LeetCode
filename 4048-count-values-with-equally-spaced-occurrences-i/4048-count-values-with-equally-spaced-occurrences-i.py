class Solution(object):
    def countSpecialIntegers(self, nums):
        d,a = {},0
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = []
            d[num].append(i)
        
        for num in d:
            if len(d[num]) == 3:
                if d[num][1] - d[num][0] == d[num][2] - d[num][1]:
                    a += 1
        
        return a