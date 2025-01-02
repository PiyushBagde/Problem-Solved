# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        hashmap = {head.val:0}
        
        while head.next != None:
            next_node = head.next
            if next_node in hashmap:
                return True

            hashmap[next_node] = 0
            head = next_node
        
        return False
            
        