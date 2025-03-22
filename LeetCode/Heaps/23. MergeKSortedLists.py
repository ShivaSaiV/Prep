# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Difficulty: hard

'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge Solution
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            # Merge pairs of lists (so basically merge sets of 2 sorted lists everytime)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                mergedLists.append(self.merge2Lists(l1, l2))
            
            lists = mergedLists
        return lists[0]
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # If one of them is empty and the other one isn't
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
    



# Heap Solution
import heapq
class Solution2(object):
    def mergeKLists(self, lists):
        
        heap = []
        # Add the first nodes to min heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        D = ListNode()
        curr = D 

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        return D.next

        

test = Solution()
print(test.mergeKLists([[1,4,5],[1,3,4],[2,6]]))
        
        