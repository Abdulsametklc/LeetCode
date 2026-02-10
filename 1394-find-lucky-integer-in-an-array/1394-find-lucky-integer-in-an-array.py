from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        freq, max1 = Counter(arr), -1
        for key, value in freq.items():
            if key == value:
                if key > max1:
                    max1 = key
        
        return max1                     