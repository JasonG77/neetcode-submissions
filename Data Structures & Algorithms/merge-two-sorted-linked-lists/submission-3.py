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
        #Optimized solution

        #start with a dummy node approach
        dummy = ListNode(0)
        #track the tail to enable additions to our linked list
        tail = dummy

        while list1 and list2: 
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            #ensure we are moving down the tail pointer as we expand the list
            tail = tail.next
        #this code accounts for edge case in which one list is longer (pick the one that is truthy)
        tail.next = list1 or list2
        
        return dummy.next