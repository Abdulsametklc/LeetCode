class Solution(object):
    def getSneakyNumbers(self, nums):
        frequency = {}
        repeated = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for num, count in frequency.items():
            if count > 1:
                repeated.append(num)
        
        return repeated