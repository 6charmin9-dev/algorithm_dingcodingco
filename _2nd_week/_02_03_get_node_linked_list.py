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


linkedList = LinkedList(5)
linkedList.append(7)
linkedList.append(10)

# linkedList.display()
print(linkedList.get(0))
print(linkedList.get(1))
print(linkedList.get(2)) 
print(linkedList.get(3)) #raise IndexError("Index out of bounds")
