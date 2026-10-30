class Solution(object):
    def distributeCandies(self, n, limit):
        a,b,c,r = 0,0,0,0
        for i in range(limit+1):
            a = i
            i +=1
            for j in range(limit+1):   
                b = j
                j +=1
                c = n - b - a
                if (0 <= a <= limit) and (0 <= b <= limit) and (0 <= c <= limit) and ((a+b+c) == n):
                    r += 1

        return r