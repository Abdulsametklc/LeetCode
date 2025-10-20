class Solution(object):
    def hammingDistance(self, x, y):
        z = x ^ y
        count = 0
        while z > 0:
            if z & 1:
                count +=1
            z = z >> 1
        return count 



        