# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val = {}
        temp = head
        while temp:
            if temp in val:
                return True
            val[temp] = True
            temp = temp.next

        return False