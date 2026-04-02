import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        limit = int(math.sqrt(n)) + 1

        for m in range(2, limit):
            for r in range(1,m):
                if math.gcd(m,r) == 1 and (m - r) % 2 == 1:
                    c = m*m + r*r
                    if c>n:
                        continue
                    
                    count += (n) // c

        return count * 2
        