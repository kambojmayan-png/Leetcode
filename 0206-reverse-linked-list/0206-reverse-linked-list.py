# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def recursion(head):
    if head == None or head.next == None:
        return head
        
    newHead = recursion(head.next)
    
    front = head.next
    front.next = head
    head.next = None

    return newHead 

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return recursion(head)