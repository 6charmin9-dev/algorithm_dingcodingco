class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 구현해보세요!
        if len(self.items) <= 2:
            return self.items.pop()
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        deleted = self.items.pop()
        idx = 1
        while idx * 2 < len(self.items):
            left_child = idx * 2
            right_child = idx * 2 + 1
            if right_child < len(self.items) and self.items[right_child] > self.items[left_child]:
                larger_child = right_child
            else:
                larger_child = left_child
            if self.items[larger_child] > self.items[idx]:
                self.items[larger_child], self.items[idx] = self.items[idx], self.items[larger_child]
                idx = larger_child
            else:
                break
        return deleted  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

# 사간복잡도: O(log N)