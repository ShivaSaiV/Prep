class Solution:
    def reorderList(self, head):
        if head is None:
            return None
        
        slow, fast = head, head.next

        # Find the middle - slow would be middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half of the linked list
        second = slow.next
        prev = slow.next = None

        # Reverse second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge 2 halves alternatively
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


# Brute Force O(n), O(n)
class Solution2:
    def reorderList(self, head):
        if head is None:
            return None
        
        curr = head
        
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None
        
