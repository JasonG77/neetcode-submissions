# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #Perform a DFS search :
            # - Ensure they are the same structure + node value
        #start with base case (both empty):
        if not p and not q:
            return True
        #Check if one of them is empty (unbalanced)
        if not p or not q: 
            return False
        #Compare raw node values
        if p.val != q.val:
            return False
        #perform DFS search for each tree (left vs right subtrees)
        #return the comparison between p and q

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

