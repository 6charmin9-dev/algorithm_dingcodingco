class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''
head: 첫번째 노드를 가리킴
tail: 마지막 노드를 가리킴
'''
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 데이터 추가하기
    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        if not self.head:
            self.head = new_node
            self.tail = self.head
        return

    # 맨 앞의 데이터 뽑기
    def dequeue(self):
        # 어떻게 하면 될까요?
        dequeued_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return dequeued_data

    def peek(self):
        # 어떻게 하면 될까요?
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None
    
queue = Queue()
queue.enqueue(1) # [1]
print(f"head: {queue.head.data}, tail: {queue.tail.data}")
print(queue.peek()) # -> 1
queue.enqueue(2) # [1, 2]
print(f"head: {queue.head.data}, tail: {queue.tail.data}")
print(queue.peek()) # -> 1
print(queue.dequeue()) # -> 1, [2] 
print(f"head: {queue.head.data}, tail: {queue.tail.data}")
print(queue.peek()) # -> 2
print(queue.dequeue()) # -> 2, []
print(f"head: {queue.head}, tail: {queue.tail}")
print(queue.is_empty()) # True
