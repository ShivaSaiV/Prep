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
        
        randoms = {}
        nexts = {}
        curr = head

        while curr:
            randoms[curr] = curr.random
            nexts[curr] = curr.next
            curr = curr.next
        
        print(randoms[0])
        print(nexts)