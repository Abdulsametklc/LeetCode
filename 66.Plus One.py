class Solution(object):
    def plusOne(self, digits):
        if 1 <= len(digits) <= 1000:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    return digits
                digits[i] = 0
            return [1] + digits