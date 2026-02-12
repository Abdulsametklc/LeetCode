class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        fark = arr[1] - arr[0]
        for i in range(1,len(arr)-1):
            if fark == arr[i+1] - arr[i]:
                pass
            else:
                return False
        return True   