# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set() #Yes - You can add Node objects to sets
        curr = head

        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
                curr = curr.next
        return False

    
        