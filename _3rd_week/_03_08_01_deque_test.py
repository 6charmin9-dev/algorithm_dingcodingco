from collections import deque
queue = deque()
queue.append(3)
queue.append(4)
print(queue.popleft())
print(queue.popleft())
# print(queue.popleft()) # IndexError: pop from an empty deque