class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

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
                if temp.next == self.head:
                    break
                index += 1
                temp = temp.next
            return index

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert(self, value, location=0):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
            self.head.next = self.tail
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = self.head
            elif location == -1:
                self.tail.next = node
                self.tail = node
                self.tail.next = self.head
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    self.tail.next = node
                    self.tail = node
                    self.tail.next = self.head
                else:
                    node.next = temp.next
                    temp.next = node

    def traverse(self):
        if self.isEmpty():
            return 'The linked list is empty'
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.head:
                    break

    def search(self, value):
        if self.isEmpty():
            return 'the linked list is empty!'
        else:
            node = self.head
            index = 0
            while node:
                if node.value == value:
                    return f'Value {value} found at index {index}'
                node = node.next
                index += 1
                if node == self.head:
                    break
            return 'Value not found in the linked list!'

    def delete(self, location):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            if location == 0:
                self.tail.next = self.head.next
                self.head = self.head.next
            elif location == -1:
                temp = self.head
                while temp:
                    if temp.next == self.tail:
                        break
                    temp = temp.next
                temp.next = self.head
                self.tail = temp
                self.tail.next = self.head
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    temp.next = self.head
                    self.tail = temp
                    self.tail.next = self.head
                else:
                    temp.next = temp.next.next

    def destroy(self):
        self.tail.next = None
        self.head = None
        self.tail = None


CSLL = CircularSinglyLinkedList()
print(CSLL.isEmpty())
CSLL.insert(1)
CSLL.insert(2)
CSLL.insert(3)
CSLL.insert(4)
print(CSLL)
CSLL.insert(5, -1)
print(CSLL)
CSLL.insert(55, 3)
print(CSLL)
print('------')
CSLL.traverse()
print(CSLL.search(4))
print('------')
print(len(CSLL))
print('------')
CSLL.delete(3)
print(CSLL)
print(CSLL.__class__.__name__)
CSLL.destroy()
print(CSLL)
