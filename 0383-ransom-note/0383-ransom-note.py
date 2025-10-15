from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_s = Counter(ransomNote)
        m_s = Counter(magazine)

        for harf, miktar in r_s.items():
            if m_s[harf] < miktar:
                return False
        return True