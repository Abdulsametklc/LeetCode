class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n] = 1 

        en_buyuk, sayac = 0, 1
        for i in freq.values():
            if en_buyuk < i:
                en_buyuk = i
                sayac = 1
            elif en_buyuk == i:
                    sayac += 1
        
        return sayac * en_buyuk