# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = l1
        mergedArr = []
        try:
            while(l1.next):
                l1 = l1.next
            l1.next = l2
            print(mergedList)
            while(mergedList.next):
                print(mergedList.val)
                mergedArr.append(mergedList.val)
                mergedList = mergedList.next
            mergedArr.append(mergedList.val)
            mergedArr.sort()
            newList = ListNode(mergedArr[0])
            newListHead = newList
            for i in range(1, len(mergedArr)):
                newList.next = ListNode(mergedArr[i])
                newList = newList.next 
            return newListHead  
        except:
            try:
                if(l1 and l2 == None):
                    return l1
                elif(l1 == None and l2):
                    return l2
            except:
                try:
                    if(l1 == None and l2):
                        return l2
                except:
                    return None
