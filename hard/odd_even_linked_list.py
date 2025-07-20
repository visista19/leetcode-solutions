class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head 
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head
    
#Key Idea (How LeetCode Expects It)
#Maintain two separate lists:
#One for odd-positioned nodes.
#One for even-positioned nodes.
#Then combine them at the end.
 # ------------------------ Explanation ------------------------

        # Input:        1 → 2 → 3 → 4 → 5
        # Step 1:       odd = 1, even = 2, even_head = 2
        #
        # 🌀 Loop:
        #   After 1st Iteration:
        #      odd = 3, even = 4
        #      List: 1 → 3 → 4 → 5
        #            ↑     ↑
        #          odd   even
        #      even_head = 2 → 4
        #
        #   After 2nd Iteration:
        #      odd = 5, even = None
        #      List: 1 → 3 → 5
        #      even_head = 2 → 4
        #
        # 🔚 Connect: 5 → 2 → 4
        #
        # Final Output: 1 → 3 → 5 → 2 → 4