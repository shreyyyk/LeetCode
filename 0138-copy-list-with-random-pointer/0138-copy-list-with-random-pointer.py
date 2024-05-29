"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper={None:None}
        cur=head
        while(cur):
            copy=Node(cur.val)
            mapper[cur]=copy
            cur=cur.next
        cur=head
        while(cur):
            copy=mapper[cur]
            copy.next=mapper[cur.next]
            copy.random=mapper[cur.random]
            cur=cur.next

        return mapper[head]