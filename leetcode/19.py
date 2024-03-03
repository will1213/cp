# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        prev = None
        while node.next:
            node.prev = prev
            prev = node
            node = node.next
        node.prev = prev
        for _ in range(n-1):
            node = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            head = head.next
        return head
