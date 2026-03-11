class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq, result = {}, []

        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in arr2:
            for i in range(freq[num]):
                result.append(num)
            del freq[num]
        
        rest = []
        for k,v in freq.items():
            for i in range(v):
                rest.append(k)

        rest.sort()

        return result + rest        