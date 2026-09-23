# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        res = head
        curr = head

        while curr:
            # Keep m nodes (step m-1 times forward)
            for _ in range(m - 1):
                if not curr:
                    break
                curr = curr.next
            if not curr:
                break
            # Skip n nodes
            skip_curr = curr.next
            for _ in range(n):
                if not skip_curr:
                    break
                skip_curr = skip_curr.next
            curr.next = skip_curr
            curr = skip_curr
        
        return res