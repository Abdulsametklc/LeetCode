class Solution(object):
    def maxFreqSum(self, s):
        unluler = "aeiou"
        unlu_sayac = {}
        unsuz_sayac = {}

        for a in s:
            if a in unluler:
                if a in unlu_sayac:
                    unlu_sayac[a] += 1
                else:
                    unlu_sayac[a] = 1
            else:
                if a in unsuz_sayac:
                    unsuz_sayac[a] += 1
                else:
                    unsuz_sayac[a] = 1
        
        if unlu_sayac:
            max_unlu = max(unlu_sayac.values())
        else:
            max_unlu = 0

        if unsuz_sayac:
            max_unsuz = max(unsuz_sayac.values())
        else:
            max_unsuz = 0

        return max_unsuz + max_unlu