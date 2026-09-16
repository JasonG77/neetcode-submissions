# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #to find the common ancestor lets think about these rules. 
        #Binary tree so its unique and ordered
        #the unique ordered property lets us assume that if the p and q are on opposite sides, root is the LCA
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            #into the loop means root is not LCA
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
    
        return root