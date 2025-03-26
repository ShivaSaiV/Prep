class Solution:
    def mergeKLists(self, lists):
        if lists is None:
            return None
        
        if len(lists) == 0:
            return None
        
        n = len(lists)
        res = []

        def merge2Lists(l1, l2):
            if l1 is None and l2 is None:
                return None
            
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                
                else:
                    tail.next = l2
                    l2 = l2.next

                tail = tail.next
            
            if l1:
                tail.next = l1
                l1 = l1.next
            if l2:
                tail.next = l2
                l2 = l2.next
            
            return dummy.next
            


        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                
                mergedLists.append(merge2Lists(l1, l2))
        
            lists = mergedLists
        
        return lists[0]
            
        

