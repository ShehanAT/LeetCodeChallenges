from collections import deque 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        currNode = []
        nextLevel = False 
        if root == None:
            return 0
        maxDepth = 0
        queue = deque([root])
        while(queue):
            n = len(queue)
            maxDepth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
        return maxDepth 
