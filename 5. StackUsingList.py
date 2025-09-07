class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
