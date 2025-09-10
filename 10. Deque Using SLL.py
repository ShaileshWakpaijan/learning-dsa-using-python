class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    
    def insert_at_last(self, data):
        # if self.is_empty():
        #     n = Node(None, data, None)
        #     self.start = n
        # else:
        #     temp = self.start
        #     while temp.next is not None:
        #         temp = temp.next
        #     n = Node(temp, data, None)
        #     temp.next = n

        # Alternative
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def insert_after(self, temp, data):
        # if temp is None:
        #     return
        # elif temp.next is None:
        #     n = Node(temp, data, temp.next)
        #     temp.next = n
        # else:
        #     n = Node(temp, data, temp.next)
        #     temp.next.prev = n
        #     temp.next = n

        # Alternative
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def insert_before(self, temp, data):
        if temp is None:
            return
        elif temp.prev is None:
            n = Node(None, data, temp)
            temp.prev = n
            self.start = n
        else:
            n = Node(temp.prev, data, temp)
            temp.prev.next = n
            temp.prev = n

    def delete_first(self):
        # if not self.is_empty():
        #     temp = self.start
        #     if temp.next is not None:
        #         temp.next.prev = None
        #         self.start = temp.next
        #     else:
        #         self.start = None

        # Alternative
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is not None:
                while temp.next is not None:
                    if temp.next.next is None:
                        break
                    temp = temp.next
                temp.next = None
            else:
                self.start = None

    # def delete_item(self, data):
    #     temp = self.start
    #     if self.is_empty():
    #         return
    #     elif temp.next is None and temp.item == data:
    #         self.start = None
    #     elif temp.prev is None and temp.item == data:
    #         temp.next.prev = None
    #         self.start = temp.next
    #     else:
    #         while temp.next is not None:
    #             if temp.item == data:
    #                 break
    #             temp = temp.next
    #         if temp.item == data and temp.next is not None:
    #             temp.prev.next = temp.next
    #             temp.next.prev = temp.prev
    #         elif temp.item == data and temp.next is None:
    #             temp.prev.next = None

    # Alternative
    def delete_item(self, data):
        if self.is_empty():
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def __iter__(self):
        return DLLItrator(self.start)

class DLLItrator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
