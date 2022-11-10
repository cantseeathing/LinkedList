class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
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

    def insert(self, value, location):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:  # at the start
                new_node.next = self.head
                self.head = new_node
            elif location == -1:  # at the end
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = None
            else:  # at other locations
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                temp_node.next = new_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            temp_node = self.head
            while temp_node is not None:
                print(temp_node.value)
                temp_node = temp_node.next

    def search(self, value):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            temp_node = self.head
            counter = 0
            while temp_node is not None:
                if temp_node.value == value:
                    return f'Value {value} is found at node {counter}'
                temp_node = temp_node.next
                counter += 1

    def deleteNode(self, location):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
            elif location == -1:
                temp_node = self.head
                while temp_node:
                    if temp_node.next == self.tail:
                        break
                    temp_node = temp_node.next
                self.tail = temp_node
                temp_node.next = None
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next

    def destroy(self):
        if self.isEmpty():
            return 'The linked list is empty!'
        else:
            self.head = None
            self.tail = None
            return 'linked list is destroyed'


LL = SinglyLinkedList()
print(LL)
print(LL.isEmpty())
LL.insert(1, 0)
LL.insert(2, 0)
LL.insert(3, 0)
LL.insert(4, 0)
print(LL)
LL.insert(5, -1)
print(LL)
LL.insert(69, 3)
print(LL)
LL.traverse()
print(LL.search(1))
LL.deleteNode(-1)
print(LL)
print(len(LL))
print(LL.destroy())
print(LL)
