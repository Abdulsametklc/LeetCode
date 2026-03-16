class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        qn = n//4
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            if freq[num] > qn:
                return num        