class Solution(object):
    def isValid(self, s):
        stack = []
        eslesen = {')': '(', ']': '[', '}': '{'}

        for karakter in s:
            if karakter in "([{":
                stack.append(karakter)
            elif karakter in ")]}":
                if not stack or stack[-1] != eslesen[karakter]:
                    return False
                stack.pop()

        return len(stack) == 0
        
        