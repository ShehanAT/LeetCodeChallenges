# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertNode(root, item) -> ListNode:
        temp = ListNode(item)
        if(root == None):
            root = temp
        else:
            ptr = root
            while(ptr.next != None):
                ptr = ptr.next
            ptr.next = temp 
        return root 
        
    def reverseList(self, head: ListNode) -> ListNode:
        storageArr = []
        try:       
            while(head.next):
                storageArr.insert(0, head.val)
                head = head.next
            storageArr.insert(0, head.val)
            print(storageArr)
            revList = ListNode(storageArr[0])
            ptr = revList 
            for i in range(1, len(storageArr)):
                temp = ListNode(storageArr[i])
                ptr.next = temp
                ptr = ptr.next
            return revList
        except:
            return None
        
