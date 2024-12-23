# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Difficulty: easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class ListNode(object):
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        if head is None:
            return None
        while curr is not None and curr.next is not None:
            v1 = curr.val
            v2 = curr.next.val
            if v1 == v2:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
