class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        node_idx = len(self.items) - 1
        parent_node_idx = node_idx // 2
        while parent_node_idx > 0 and self.items[parent_node_idx] < self.items[node_idx]:
            self.items[parent_node_idx], self.items[node_idx] = self.items[node_idx], self.items[parent_node_idx]
            node_idx = parent_node_idx
            parent_node_idx = node_idx // 2

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!