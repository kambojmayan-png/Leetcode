# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2list(self, list1, list2):
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next

            head = head.next

        if list1:
            head.next = list1

        if list2:
            head.next = list2

        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.merge2list(l1, l2))

            lists = mergedList

        return lists[0]