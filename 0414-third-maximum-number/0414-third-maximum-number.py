class Solution(object):
    def heap(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2 

        if left < n and nums[left] > nums[largest]:
            largest = left
        
        if right < n and nums[right] > nums[largest]:
            largest = right
        
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heap(nums, n, largest)

    def thirdMax(self, nums):
        nums = list(set(nums))
        n = len(nums)

        for i in range(n//2 -1, -1, -1):
            self.heap(nums, n, i)
        
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heap(nums, i, 0)
            
        if len(nums) < 3:
            return nums[len(nums)-1]
        
        return nums[len(nums)-3]
