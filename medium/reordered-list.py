# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        stack=[]
        current = head
        while current:
            stack.append(current)
            current=current.next
        n= len(stack)
        current = head
        for _ in range(n//2):
            end=stack.pop()
            next_node=current.next
            current.next=end
            end.next=next_node
            current=next_node
        current.next=None