
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validBST_helper(root, float("-inf"), float("inf"))
    
    def validBST_helper(self, root, min_val, max_val):
        if root is None:
            return True # reached the end of binary tree
        if root.val <= min_val or root.val >= max_val:
            return False # test if sub tree is balanced 
        return self.validBST_helper(root.left, min_val, root.val) and self.validBST_helper(root.right, root.val, max_val)
        # first return call for left side validation
        # second return call for right side validation 
