# https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: easy

'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        num = head
        count = 0

        while num:
            count += 1
            num = num.next

        print(count)

        curr = head
        middle = count / 2
        n = 0
        
        while curr:
            if n == middle:
                return curr
            curr = curr.next
            n += 1

        