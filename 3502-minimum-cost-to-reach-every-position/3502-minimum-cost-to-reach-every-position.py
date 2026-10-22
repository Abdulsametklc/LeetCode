class Solution(object):
    def minCosts(self, cost):
        k, u = 100, len(cost)
        for i in range(u):
            if k > cost[i]:
                k = cost[i]
                
            cost[i] = k

        return cost