class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters)-1
        ans = -1

        while l <= r:
            mid = (l+r)//2
            if letters[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return letters[0] if ans == -1 else letters[ans]           