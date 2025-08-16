class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        else:
            print("None")

    def get(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
            if (cur is None):
                raise IndexError("Index out of bounds")
        return cur.data

    def add(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self.head
        for i in range(index-1):
            prev_node = prev_node.next
            if prev_node is None:
                raise IndexError("Index out of bounds")
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete(self, index):
        if index == 0:
            if self.head.next is None:
                raise IndexError("head cannot be None")
            self.head = self.head.next
            return
        prev_node = self.head
        for i in range(index-1):
            prev_node = prev_node.next
            if prev_node is None or prev_node.next is None:
                raise IndexError("Index out of bounds")
        prev_node.next = prev_node.next.next



'''
0    1    2
5 -> 7 -> 10

0    1    2    3
5 -> 2 -> 7 -> 10
'''


linkedList = LinkedList(5)
linkedList.append(7)
# linkedList.append(10)

linkedList.delete(0)
# linkedList.delete(1)
# linkedList.delete(2)
linkedList.display()
