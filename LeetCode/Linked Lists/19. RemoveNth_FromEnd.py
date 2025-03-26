# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Difficulty: medium

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        
        total_n = 0
        curr = head

        while curr:
            total_n += 1
            curr = curr.next
        ind = total_n - n 

        if total_n == 1 and n == 1:
            return None
        
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy

        for i in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
            

# Iterative 2pass:
class Solution(object):
    def removeNthFromEnd(self, head, n):
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        
        removeIndex = N - n
        if removeIndex == 0:
            return head.next
        
        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
            

# 2 Pass
class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        
        N = 0
        curr = head

        while curr:
            N += 1
            curr = curr.next
        
        idx = N - n

        if idx == 0:
            return head.next

        curr = head
        for i in range(N - 1):
            if (i + 1) == idx:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head
