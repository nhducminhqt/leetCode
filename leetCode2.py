class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def MTL(self,list1,list2):
        head = ListNode()
        p = head
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1.val
                list1 = list1.next
            else:
                p.next = list2.val
                list2 = list2.next
        if list1:
            p.next = list1
        elif list2:
            p.next = list2
        return head.next