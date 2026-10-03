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
        OldNode = {}

        cur = head
        while cur:
            copy = Node(cur.val)
            OldNode[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = OldNode[cur]
            copy.next = OldNode.get(cur.next)
            copy.random = OldNode.get(cur.random)
            cur = cur.next

        return OldNode.get(head)