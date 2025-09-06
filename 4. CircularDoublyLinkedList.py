class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start = None):
        self.start = start

    def isEmpty(self):
        return self.start == None
    
    def printList(self):
        if not self.isEmpty():
            temp = self.start
            while temp is not self.start.prev:
                print(temp.item, end=" <--> ")
                temp = temp.next
            print(temp.item)
    
    def search(self, data):
        if self.isEmpty():
            return
        if self.start.next == self.start and self.start.item == data:
            return self.start
        temp = self.start
        while temp is not self.start.prev:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp

    def insertAtFirst(self, data):
        n = Node(item = data)
        if self.isEmpty():
            n.prev = n
            n.next = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
    
    def insertAtLast(self, data):
        n = Node(item=data)
        if self.isEmpty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n

    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            temp.next.prev = n
            temp.next = n

    def deleteFirst(self):
        if self.isEmpty():
            return
        if self.start.next == self.start:
            self.start = None
            return
        self.start.next.prev = self.start.prev
        self.start.prev.next = self.start.next
        self.start = self.start.next
    
    def deleteLast(self):
        if self.isEmpty():
            return
        if self.start.next == self.start:
            self.start = None
            return
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev

    def deleteItem(self, data):
        if self.isEmpty():
            return
        if self.start.item == data:
            self.deleteFirst()
        elif self.start.prev.item == data:
            self.deleteLast()
        else:
            temp = self.start
            while temp is not self.start.prev:
                if temp.item == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break
                temp = temp.next

    def __iter__(self):
        if self.isEmpty():
            return CDLLItator(None)
        else:
            return CDLLItator(self.start)

class CDLLItator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current is self.start and self.count == 1:
            raise StopIteration
        self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data
