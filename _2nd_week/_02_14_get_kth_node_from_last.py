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

    # 링크드 리스트 끝에서 K 번째 값 출력하기
    def get_kth_node_from_last2(self, k):
        # 구현해보세요!
        slow = self.head
        fast = self.head
        for i in range(k):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        curr = self.head
        arr = []
        while curr is not None:
            arr.append(curr)
            curr = curr.next
        return arr[-k]  


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last2(2).data)  # 7이 나와야 합니다!