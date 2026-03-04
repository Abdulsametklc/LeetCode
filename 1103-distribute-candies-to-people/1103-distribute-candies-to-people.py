class Solution(object):
    def distributeCandies(self, candies, num_people):
        dist, i, k = [0] * num_people, 0, 1
        while candies > 0:
            if candies < k:
                k = candies
            dist[i] += k
            candies -= k
            i += 1
            k += 1
            if i == num_people:
                i = 0
        return dist    