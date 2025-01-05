# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0

        while head != None:
            num = num * 10 + head.val
            head = head.next
        
        res = 0
        pov = 0

        while num != 0:
            rem = num % 10
            res += rem * (2**pov)
            pov += 1
            num = num // 10
        
        return res



        