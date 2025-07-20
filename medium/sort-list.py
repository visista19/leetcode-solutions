# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        # Step 1: Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Split the list
        mid = slow.next
        slow.next = None
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        # Step 3: Merge two sorted halves
        return self.merge(left, right)
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Attach remaining nodes
        tail.next = l1 or l2
        return dummy.next
        