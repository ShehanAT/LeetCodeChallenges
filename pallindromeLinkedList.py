# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        try:
            while(head.next):
                arr.append(head.val)
                head = head.next 
            arr.append(head.val)
            print(arr)
            if len(arr) == 1:
                return True
            if arr == arr[::-1]:
                return True 
            else:
                return False 
        except:
            return True 
