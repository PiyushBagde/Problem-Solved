# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        curr = root.left

        def invert(curr):
            if curr is None:
                return curr
            
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            invert(curr.left)
            invert(curr.right)

        invert(curr)

        #compare

        def comp(p,q):
            if p==None  and q == None:
                return True
            
            if p==None  or q == None:
                return False
            
            if p.val == q.val and comp(p.left, q.left) and comp(p.right, q.right):
                return True
            return False

        return comp(root.left, root.right)