class Solution(object):
    def countLargestGroup(self, n):
        groups = {}
        for i in range(1, n + 1):
            digit_sum = sum(int(c) for c in str(i))
            
            if digit_sum in groups:
                groups[digit_sum] += 1
            else:
                groups[digit_sum] = 1

        max_size = max(groups.values())
        count = 0
        for value in groups.values():
            if value == max_size:
                count += 1

        return count