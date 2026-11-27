class Solution(object):
    def countDominantElements(self, nums):
        a, counter = len(nums), 0

        if a == 1:
            return 1

        for i in range(a):
            if i == 0:
                if nums[i] >= nums[i+1]:
                    counter += 1
                continue

            if i == a-1:
                if nums[i] >= nums[i-1]:
                    counter += 1
                continue
            
            if 2*nums[i] >= nums[i-1] + nums[i+1]:
                counter +=1
        
        return counter