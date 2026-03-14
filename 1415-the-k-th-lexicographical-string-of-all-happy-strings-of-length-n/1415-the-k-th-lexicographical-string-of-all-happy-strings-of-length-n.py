class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def dfs(path):
            if len(path) == n:
                res.append(path)
                return
            
            for ch in "abc":
                if not path or path[-1] != ch:
                    dfs(path + ch)
        
        dfs("")

        if k > len(res):
            return ""
        
        return res[k-1]