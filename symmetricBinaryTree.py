class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.nodeSymmetric(root, root)
    
    def nodeSymmetric(self, leftNode, rightNode):
        if(leftNode is None and rightNode is None):
            return True
        else:
            if(leftNode and rightNode):
                if(leftNode.val == rightNode.val):
                        return self.nodeSymmetric(leftNode.left, rightNode.right) and self.nodeSymmetric(leftNode.right, rightNode.left)
            else:
                return False 
            