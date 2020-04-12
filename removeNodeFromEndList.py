# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenCounter, curr, head =  head, head, head
        listLen = 1
        while(lenCounter.next):
            lenCounter = lenCounter.next
            listLen += 1
        if listLen == 1:
            head = None
            return head 
        index = listLen - n
        if listLen - index == 1:
            for i in range(1, index):
                curr = curr.next
            curr.next = None
            return head 
        elif index == 0:
            head = head.next
            return head
        else:
            for i in range(1, index):
                curr = curr.next
            try:
                curr.next = curr.next.next
            except:
                curr.val = curr.next.val
                curr.next = None
            return head
        