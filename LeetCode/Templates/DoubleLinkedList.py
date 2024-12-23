class DoublyNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)


head = tail = DoublyNode(1)
A = DoublyNode(2)
B = DoublyNode(3)
head.next = A
A.prev = head
A.next = B 
B.prev = A
tail = B
print(tail)

# Display - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(head)

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
    newNode = DoublyNode(val)
    newNode.next = head
    head.prev = newNode
    return newNode, tail

head, tail = insert_at_beginning(head, tail, 0)
display(head)

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    newNode = DoublyNode(val)
    tail.next = newNode
    newNode.prev = tail
    return head, newNode

head, tail = insert_at_end(head, tail, 10)
display(head)
