class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow.")
        last = self.items.pop(0)
        return last

    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow.")

    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow.")
    
    def size(self):
        return len(self.items)
