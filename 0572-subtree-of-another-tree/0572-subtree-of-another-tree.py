# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if (not s) and (not t):
            return True
        
        if (s and t) and (s.val == t.val):
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        