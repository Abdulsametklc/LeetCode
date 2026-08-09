class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        t1, t2 = "", ""
        for i in range(len(word1)):
            t1 += word1[i]
        
        for k in range(len(word2)):
            t2 += word2[k]
            
        return t1 == t2