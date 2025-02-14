class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next  # Move slow by one step
            fast = fast.next.next  # Move fast by two steps

            # If slow and fast meet, a cycle exists
            if slow == fast:
                return True

        # If we reach the end, no cycle exists
        return False