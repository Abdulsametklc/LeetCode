class Solution(object):
    def isSameTree(self, p, q):
        
        def traverse(p,q):

            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return traverse(p.left, q.left) and traverse(p.right, q.right)

        return traverse(p,q)           