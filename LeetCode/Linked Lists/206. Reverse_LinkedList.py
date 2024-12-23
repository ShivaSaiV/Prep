# https://leetcode.com/problems/reverse-linked-list/description/
# Difficulty: easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        curr = head
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev