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