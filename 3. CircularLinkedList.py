class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last = None):
        self.last = last
        
    def isEmpty(self):
        return self.last == None
    
    def printList(self):
        if self.isEmpty(): 
            return
        else:
            temp = self.last.next
            while temp is not self.last:
                print(temp.item, end='➡ ')
                temp = temp.next
            print(temp.item)
            
    def search(self, data):
        if self.isEmpty():
            return None
        else:
            temp = self.last.next
            while temp is not self.last:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
            else:
                return None
            
    def insertAtStart(self, data):
        if self.isEmpty():
            n = Node(data)
            n.next = n
            self.last = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n
    
    def insertAtLast(self, data):
        if self.isEmpty():
            n = Node(data)
            n.next = n
            self.last = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n
            self.last = n

    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp is self.last:
                self.last = n

    def deleteFirst(self):
        if self.isEmpty():
            return
        if self.last.next is not self.last:
            self.last.next = self.last.next.next
        else:
            self.last = None

    def deleteLast(self):
        if self.isEmpty():
            return
        if self.last.next is self.last:
            self.last = None
        else:
            temp = self.last.next
            while temp.next is not self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp
            
    def deleteItem(self, data):
        if self.isEmpty():
            return
        if self.last.next is self.last and self.last.item != data:
            return
        if self.last.item == data:
            self.deleteLast()
        elif self.last.next.item == data:
            self.deleteFirst()
        else:
            temp = self.last.next
            while temp is not self.last:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
            
    def __iter__(self):
        if self.last is None:
            return CLLItrator(None)
        else:
            return CLLItrator(self.last.next)

class CLLItrator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
         
        if self.current == self.start and self.count == 1:
            raise StopIteration
        self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data
