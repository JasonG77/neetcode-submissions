# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #perform BST
        #queue and inside its a list(S), and add to it as we traverse through the tree
        #base case
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            levelSize = len(queue)
            curLevel = []
            for _ in range(levelSize):
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curLevel)
        
        return result


