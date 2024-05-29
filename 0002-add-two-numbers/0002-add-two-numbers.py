# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry=0
        head=ListNode()
        cur=head
        while(l1 or l2 or carry):
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            val=l1val+l2val + carry
           
            carry=val//10
            val=val%10
            cur.next=ListNode(val)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next