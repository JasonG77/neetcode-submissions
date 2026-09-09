# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Think how can you combine them in the fastest manner 
        #Prioritize runtime over space complexity
        
    
        #traverse both lists -> [1, 2, 4] and [1, 3, 5]
        newList = []
        while list1:
            newList.append(list1.val)
            list1 = list1.next 
        while list2: 
            newList.append(list2.val)
            list2 = list2.next

        newList.sort()

        dummy = ListNode(0)
        tail = dummy
        for item in newList:
            tail.next = ListNode(item)
            tail = tail.next

        return dummy.next