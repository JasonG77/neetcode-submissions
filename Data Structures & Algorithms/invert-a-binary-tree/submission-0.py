# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #account for the edge case where the nodes are null
        if not root:
            return None

        #start by flipping / reversing the tree nodes left and right branches
        temp = root.right
        root.right = root.left
        root.left = temp

        #now recruse through the right and left subtrees
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root