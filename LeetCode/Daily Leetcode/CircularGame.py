class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            newNode.next = newNode
            self.head = newNode
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode 
            newNode.next = self.head

    def deleteNode(self, data):
        if self.head is None:
            return
        
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return

        last = self.head

        if self.head.data == data:
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = last.next
            return

        while last.next != self.head and last.next.data != data:
            last = last.next

        if last.next.data == data:
            last.next = last.next.next
        else:
            print("Node not found")

    def countNodes(self):
        if self.head is None:
            return 0
        temp = self.head
        result = 1
        while temp.next != self.head:
            result += 1
            temp = temp.next
        return result

class Solution(object):
    def findTheWinner(self, n, k):
        # for i in range(1, n + 1):
        #     circle.append(i)

        # while (len(circle) != 1):
        #     if (start >= n):
        #         break
        #     start += k - 1
        #     print(start)

        #     circle.remove(start)

        #     start += 1

        circularList = CircularLinkedList()
        for i in range(1, n + 1):
            circularList.append(i)

        curr = circularList.head

        

        while (circularList.countNodes() > 1):
            start = 1
            while start != k:
                curr = curr.next
                start += 1

            circularList.deleteNode(curr.data)
            curr = curr.next

            # if curr.data == start:
            #     circularList.deleteNode(curr)
            # start += 1
            # print(curr.data)
            # curr = curr.next

            # if curr == circularList.head:
            #     break

        winner = curr.data
            

        return winner
    
test = Solution()
print(test.findTheWinner(5, 2))