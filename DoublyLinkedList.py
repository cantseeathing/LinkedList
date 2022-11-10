class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        if self.isEmpty():
            return 'linked list is empty'
        values = [str(x.value) for x in self]
        return ' '.join(values)

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.head
            index = 1
            while temp:
                if temp == self.tail:
                    break
                index += 1
                temp = temp.next
            return index

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert(self, value, location=0):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == -1:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:
                    node.next = temp.next
                    temp.next.prev = node
                    node.prev = temp
                    temp.next = node

    def traverse(self, inverse=False):
        if self.isEmpty():
            return 'linked list is empty'
        else:
            if not inverse:
                temp = self.head
                while temp:
                    print(temp.value)
                    if temp == self.tail:
                        break
                    temp = temp.next
            else:
                temp = self.tail
                while temp:
                    print(temp.value)
                    if temp == self.head:
                        break
                    temp = temp.prev

    def print_details(self):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            node = self.head
            print('Value\tNext\tPrevious')
            while node:
                try:
                    print(f'{node.value}\t\t{node.next.value}\t\t{node.prev.value}')
                except AttributeError:
                    if node == self.head:
                        print(f'{node.value}\t\t{node.next.value}\t\tNone')
                    else:
                        print(f'{node.value}\t\tNone\t{node.prev.value}')
                if node == self.tail:
                    break
                node = node.next

    def search(self, value):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            temp = self.head
            index = 0
            while temp:
                if temp.value == value:
                    return f'Value {value} found at index {index}'
                if temp == self.tail:
                    return 'Value NOT found!'
                index += 1
                temp = temp.next

    def delete(self, location):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            if location == 0:
                self.head = self.head.next
                self.head.prev = None
            elif location == -1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def destroy(self):
        if self.isEmpty():
            return 'The linked list is empty'
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            return 'Linked list was destroyed'


DLL = DoublyLinkedList()
print(DLL.isEmpty())
DLL.insert(1)
DLL.insert(2)
DLL.insert(3)
DLL.insert(4, 0)
DLL.insert(5, -1)
print(DLL)
DLL.insert(55, 3)
DLL.insert(66, 3)
print(DLL)
print(len(DLL))
print('------')
DLL.traverse()
print('------')
DLL.traverse(inverse=True)
print('------')
print(DLL)
print('------')
DLL.insert(6, 7)
print(DLL)
DLL.print_details()
print('------')
print(DLL.search(55))
print('------')
print(DLL)
DLL.delete(0)
DLL.print_details()
print('------')
print(DLL)
DLL.delete(-1)
DLL.print_details()
print('------')
print(DLL)
DLL.delete(3)
DLL.print_details()
print(DLL.destroy())
print(DLL)