class Solution(object):
    def uniqueOccurrences(self, arr):
        freq =  {}
        for n in arr:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        a = len(freq)
        b = len(set(freq.values()))
        if a == b:
            return True
        else:
            return False