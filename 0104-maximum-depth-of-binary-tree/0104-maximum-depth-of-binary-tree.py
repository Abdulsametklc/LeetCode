class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return self.count(root)
    
    def count(self, root):
        if root is  None:
            return 0
        return 1 + max(self.count(root.right), self.count(root.left))