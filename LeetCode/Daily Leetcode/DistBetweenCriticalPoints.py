# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head is None:
            return [-1, -1]
        
        if head.next is None:
            return [-1, -1]

        if head.next.next is None:
            return [-1, -1]
        
        
        minDist = 100000
        maxDist = 0

        curr = head.next
        prev = head
        critical = []
        index = 0

        while (curr.next != None):
            index += 1
            if (curr.val > prev.val) and (curr.val > curr.next.val):
                critical.append(index)
            
            if (curr.val < prev.val) and (curr.val < curr.next.val):
                critical.append(index)

            prev = curr
            curr = curr.next


        print(critical)

        if len(critical) == 0:
            return [-1, -1]

        if len(critical) == 1:
            return [-1, -1]

        critical.sort()


        if len(critical) > 1:
            maxDist = critical[-1] - critical[0]

        for i in range(len(critical) - 1):
            dist = critical[i + 1] - critical[i]
            minDist = min(minDist, dist)
        
        return [minDist, maxDist]
        