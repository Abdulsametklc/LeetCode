class Solution(object):
    def convertBST(self, root):
        if root is None:
            return None
            
        self.toplam = 0
        def traverse(currentNode):
            if currentNode.right is not None:
                traverse(currentNode.right) 

            self.toplam += currentNode.val
            currentNode.val = self.toplam 

            if currentNode.left is not None:
                traverse(currentNode.left)

        traverse(root)
        return root