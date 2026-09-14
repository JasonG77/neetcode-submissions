# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #return true if 
        def balanced(root):
            #start with base case
            if not root:
                return 0
            left = balanced(root.left) #recurse through left subtree
            if left == -1:
                return -1
            right = balanced(root.right) #recurse through right subtree
            if right == -1:
                return -1
            #do a check at every node (left vs right balance)
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right) #return the heights of each node to parent

        return balanced(root) != -1
