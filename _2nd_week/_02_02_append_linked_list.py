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

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.display()
