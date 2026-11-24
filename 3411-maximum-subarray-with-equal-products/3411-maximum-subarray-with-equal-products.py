
class Solution:

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def maxLength(self, nums):
        max_len = 0

        for i in range(len(nums)):
            prod = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):
                num = nums[j]

                prod *= num
                g = self.gcd(g, num)
                l = self.lcm(l, num)

                if prod == g * l:
                    max_len = max(max_len, j - i + 1)

        return max_len