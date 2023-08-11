# Implementing Vector class that contains all the functions mentioned


class Vector: 
    def __init__(self):
        self.capacity = 16
        arr = [] * self.capacity
        self.size = 0

    # 1. size() - Returns the number of items in the vector

    def size(self):
        print(self.size)
        return self.size
    

    # 2. capacity() - Returns the current capacity of the vector

    def capacity(self):
        print(self.capacity)
        return self.capacity
    

    # 3. is_empty() - Checks if the vector is empty

    def is_empty(self):
        return self.size == 0


    # 4. at(index) - Returns the item at the given index  

    def at(self, index):
        return self.arr[index]
    
    
    # 5. push(item) - Adds an item at the end

    def push(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.arr[self.size] = element
        self.size += 1

    
    # 6. insert(index, item) - Inserts item at the given index

    def insert(self, index, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = item
        self.size += 1


    # 7. prepend(item) - Adds an item at the beginning

    def prepend(self, item):
        self.arr(0, item)
    

    # 8. pop() - Removes the last item 

    def pop(self):
        item = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return item
    
    def fin():
        arrau = [2, 3, 4, 6]
        arrau.pop()
        print(arrau)

    fin()


    # pop() can also remove from the index

    arrau = [2, 3, 4, 6]
    arrau.pop(2)
    print(arrau)

    # 9. delete(index) - Deletes an item at a given index

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds!")
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        return self.arr


    # 10. Python List remove(): The remove() method removes the first matching element (which is passed as an argument) from the list.

    def remove(self, item):
        i = 0
        while i < self.size:
            if self.arr[i] == item:
                self.delete(i)
            else:
                i += 1


    # 11. find(item) - Finds the first occurrence of an item

    def find(self, item):
        for i in range(self.size):
            if self.arr[i] == item:
                return i
        return -1
