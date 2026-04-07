class Solution(object):
    def checkIfPangram(self, sentence):
        if 26 == len(set(sentence)):
            return True
        return False