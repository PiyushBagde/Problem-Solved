# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        res = []

        def trav(root):
            if root is None:
                return None
            
            trav(root.left)
            trav(root.right)
            res.append(root.val)

        trav(root)
        return res