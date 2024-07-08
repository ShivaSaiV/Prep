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