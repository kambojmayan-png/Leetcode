# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        while stack:
            temp.val = stack.pop()
            temp = temp.next

        return head