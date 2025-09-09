class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, data):
        n = Node(data)
        if self.isEmpty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count += 1
    
    def print_list(self):
        temp = self.front
        while temp is not None:
            print(temp.item, end = "⬅")
            temp = temp.next
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")
        elif self.front is self.rear:
            last = self.front.item
            self.front = None
            self.rear = None
        else:
            last = self.front.item
            self.front = self.front.next
        self.count -= 1
        return last
        
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")
        return self.front.item

    def getRear(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")
        return self.rear.item
