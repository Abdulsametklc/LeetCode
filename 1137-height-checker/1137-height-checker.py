class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        n, sayac = len(expected), 0
        for i in range(n-1):
            for j in range(n-i-1):
                if expected[j] > expected[j+1]:
                    expected[j], expected[j+1] = expected[j+1], expected[j]
        
        for i in range(0,n):
            if expected[i] != heights[i]:
                sayac += 1

        return sayac