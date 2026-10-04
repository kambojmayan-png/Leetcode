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
        Oldnode = { None : None }

        cur = head
        while cur:
            copy = Node(cur.val)
            Oldnode[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = Oldnode[cur]
            copy.next = Oldnode[cur.next]
            copy.random = Oldnode[cur.random]
            cur = cur.next

        return Oldnode[head] 