# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def traverse(node):
            if node == None:
                return None
        
            traverse(node.left)
            arr.append(node.val)
            traverse(node.right)

        traverse(root)

        return arr

        