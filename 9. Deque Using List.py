class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def getFront(self):
        if self.isEmpty():
            raise IndexError("Deque Undeflow")
        else:
            return self.items[0]
        
    def getRear(self):
        if self.isEmpty():
            raise IndexError("Deque Undeflow")
        else:
            return self.items[-1]
    
    def insertAtFront(self, data):
        self.items.insert(0, data)
    
    def insertAtRear(self, data):
        self.items.append(data)

    def deleteAtFront(self):
        if self.isEmpty():
            raise IndexError("Deque Underflow")
        else:
            return self.items.pop(0)
    
    def deleteAtRear(self):
        if self.isEmpty():
            raise IndexError("Deque Underflow")
        else:
            return self.items.pop()
        