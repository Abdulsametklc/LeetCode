class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        res = [""] * len(words)

        for word in words:
            index = int(word[-1])
            res[index - 1] = word[:-1]
        
        return " ".join(res)