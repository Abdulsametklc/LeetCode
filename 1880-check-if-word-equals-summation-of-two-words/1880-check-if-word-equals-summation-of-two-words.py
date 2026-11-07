class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        words = [firstWord, secondWord, targetWord]
        numbers = []

        for word in words:
            number = ""
            for char in word:
                number += str(ord(char) - ord('a'))
            numbers.append(int(number))

        if numbers[0] + numbers[1] == numbers[2]:
            return True
        return False