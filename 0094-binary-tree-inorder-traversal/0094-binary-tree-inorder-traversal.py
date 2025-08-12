class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(index, arr):
    if index >= len(arr) or arr[index] is None:
        return None
    node = TreeNode(arr[index])
    node.left = build_tree(2 * index + 1, arr)
    node.right = build_tree(2 * index + 2, arr)
    return node

class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
       
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


arr = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = build_tree(0, arr)


sol = Solution()
result = sol.inorderTraversal(root)
print(result)      