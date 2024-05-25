"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        current = root

        while current:

            dummy=Node(0)
            tail=dummy

            while current:
                if(current.left):
                    tail.next=current.left
                    tail=tail.next
                if(current.right):
                    tail.next=current.right
                    tail=tail.next
                current=current.next
            current=dummy.next
        return root