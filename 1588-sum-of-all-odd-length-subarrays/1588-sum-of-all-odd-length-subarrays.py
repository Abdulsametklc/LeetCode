class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        toplam = 0
        n = len(arr)
        for i in range(n):
            left = i + 1
            right = n - i 
            total = left * right 

            odd = (total + 1) // 2

            toplam += arr[i] * odd
        return toplam      