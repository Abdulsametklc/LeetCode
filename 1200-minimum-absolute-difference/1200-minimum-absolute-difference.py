class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        mini = float('inf')
        ans = []

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]

            if diff < mini:
                mini = diff
                ans = [[arr[i], arr[i+1]]]
            
            elif diff == mini:
                ans.append([arr[i], arr[i+1]])
        
        return ans