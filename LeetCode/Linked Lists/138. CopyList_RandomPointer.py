# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Difficulty: medium

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        
        hmap = {}
        curr = head

        # 1st run: copy and store values in hmap
        while curr:
            newNode = Node(curr.val)
            hmap[curr] = newNode
            curr = curr.next
        
        # 2nd run: use hashmap to assign newNode's next and random
        curr = head
        while curr:
            newNode = hmap[curr]
            if curr.next:
                newNode.next = hmap[curr.next]
            if curr.random:
                newNode.random = hmap[curr.random]
            curr = curr.next
        return hmap[head]