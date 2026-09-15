# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subtree): #flag subtree (subRoot)
            if not root and not subtree:
                return True
            if not root or not subtree:
                return False
            if root.val != subtree.val:
                return False
            return sameTree(root.left, subtree.left) and sameTree(root.right, subtree.right)
        #the overall algorithm to traverse thru a two trees
        if not subRoot:
            return True
        if not root:
            return False
        #perform the sameTree at the Start
        if sameTree(root, subRoot):
            return True
        #if not then check the rest of the main Tree (left and right candidates)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
        
            