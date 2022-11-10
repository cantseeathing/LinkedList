class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
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
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            if location == 0:
                self.head.prev = node
                self.tail.next = node
                node.next = self.head
                self.head = node
            elif location == -1:
                self.head.prev = node
                self.tail.next = node
                node.prev = self.tail
                node.next = self.head
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    self.head.prev = node
                    self.tail.next = node
                    node.prev = self.tail
                    node.next = self.head
                    self.tail = node
                else:
                    node.next = temp.next
                    node.prev = temp
                    temp.next.prev = node
                    temp.next = node

    def traverse(self, inverse=False):
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
                    return f'The value {value} found at index {index}'
                if temp == self.tail:
                    return 'Value NOT found!'
                index += 1
                temp = temp.next

    def delete(self, location):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            if location == 0:
                self.tail.next = self.head.next
                self.head.next.prev = self.tail
                self.head = self.head.next
            elif location == -1:
                self.tail.prev.next = self.head
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp == self.tail:
                    self.tail.prev.next = self.head
                    self.head.prev = self.tail.prev
                    self.tail = self.tail.prev
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

    def destroy(self):
        temp = self.head
        while temp:
            temp.prev = None
            if temp == self.tail:
                break
            temp = temp.next
        self.head = None
        self.tail = None


CDLL = CircularDoublyLinkedList()
print(CDLL)
print(CDLL.isEmpty())
CDLL.insert(1)
CDLL.insert(2)
CDLL.insert(3)
CDLL.insert(4)
print(CDLL)
CDLL.insert(5, 0)
print(CDLL)
CDLL.insert(6, -1)
print(CDLL)
CDLL.insert(55, 3)
print(CDLL)
CDLL.insert(66, 3)
print(CDLL)
print('-----')
CDLL.print_details()
print('-----')
CDLL.traverse(inverse=False)
print('-----')
CDLL.traverse(inverse=True)
print('-----')
print(CDLL.search(55))
print('------')
print(CDLL)
CDLL.delete(5)
print(CDLL)
print('!!!!')
CDLL.destroy()
print(CDLL)
