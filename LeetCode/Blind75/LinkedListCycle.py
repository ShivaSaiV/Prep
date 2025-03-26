# Dictionary Solution
class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        myDict = {}
        curr = head

        while curr:
            if curr in myDict:
                return True

            myDict[curr] = 1
            curr = curr.next
        
        return False
        

# 2 Pointer solution
class Solution2:
    def hasCycle(self, head):
        if head is None:
            return False
        
        fastPointer = head
        slowPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        
        return False
