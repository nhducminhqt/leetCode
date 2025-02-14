class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Nếu danh sách rỗng hoặc chỉ có 1 node, không cần hoán đổi
        if not head or not head.next:
            return head
        
        # Dùng một dummy node làm điểm bắt đầu
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = p1.next
        while p2 and p2.next:
            tmp = p2.next
            p2.next = tmp.next
            tmp.next = p2
            p1.next = tmp
            p2 = p2.next
            p1 = p1.next.next     
        return dummy.next
