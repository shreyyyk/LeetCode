# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow=head
        fast=head
        while(slow.next!=None and ( fast.next!=None and fast.next.next!=None )):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                break
        if not fast.next or not fast.next.next:
            return
        slow2=head
        while(slow2!=slow):
            slow=slow.next
            slow2=slow2.next
        
        return slow2

       

