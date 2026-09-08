# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Goal: Reverse the linked list
        #Algorithm: Reassign arrows as we go down the linked list
        
        #[0 -> 1 -> 2 -> 3 -> None] -> [None <- 0 <- 1 <- 2 <- 3]
        #[] - > []
        #We reference both linked lists by their head list node
        
        #Keep track of the current node - starts at head
        curr = head
        #keep track of the previous node and use it to reassign arrows
        prev = None 
        
        #loop to keep track of when we have surpassed the linked list length
        while curr:
            #keep track of next before we reassign (don't lose it!)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev 

