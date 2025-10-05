class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        return abs(self.balanced(root.left) - self.balanced(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def balanced(self, root):
        if root is  None:
            return 0
        return 1+max(self.balanced(root.right), self.balanced(root.left))