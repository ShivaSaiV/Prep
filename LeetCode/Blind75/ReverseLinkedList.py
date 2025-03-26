class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        dummy = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = dummy
            dummy = curr
            curr = temp
        return dummy
