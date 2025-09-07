class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.itemCount = 0

    def isEmpty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.itemCount += 1
    
    def pop(self):
        if not self.isEmpty():
            last = self.start.item
            self.start = self.start.next
            self.itemCount -= 1
            return last
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return self.itemCount
