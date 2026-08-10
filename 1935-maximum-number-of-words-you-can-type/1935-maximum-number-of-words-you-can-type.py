class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        count = 0
        for word in text.split():
            bozuk = False

            for letter in brokenLetters:
                if letter in word:
                    bozuk = True
                    break

            if not bozuk:
                count += 1
        return count