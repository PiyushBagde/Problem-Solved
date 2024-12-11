# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def addNode(arr, low, high):
            if low > high:
                return None

            mid = (low + high) // 2
            node = TreeNode(val=arr[mid])

            node.left = addNode(arr, low, mid-1)
            node.right = addNode(arr, mid+1, high)

            return node


        if len(nums) == 0:
            return None

        low , high = 0, len(nums) -1

        head = addNode(nums, low, high)


        return head


        

        