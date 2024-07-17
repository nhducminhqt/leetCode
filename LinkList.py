class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution(object):
    def DD(self,head):
        p = head
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p=p.next.val
        return head
