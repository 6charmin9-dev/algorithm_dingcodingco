class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self): # 1
        # 어떻게 하면 될까요?
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head.data

    def peek(self):
        # 어떻게 하면 될까요?
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None
        
stack = Stack()
stack.push(1)
print(f"peek: {stack.peek()}") # 1
stack.push(2)
print(f"peek: {stack.peek()}") # 2
stack.push(3)
print(f"peek: {stack.peek()}") # 3
stack.pop()
print(f"peek: {stack.peek()}") # 2
print(f"is_empty: {stack.is_empty()}") # False
stack.pop()
stack.pop()
print(f"is_empty: {stack.is_empty()}") # True



