class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()
linked_tuple.add("333", 7)
linked_tuple.add("77", 6)
print(f"linked_tuple.items: {linked_tuple.items}") # [('333', 7), ('77', 6)]
print(f"linked_tuple.get(\"77\"): {linked_tuple.get("77")}") # 6
print(f"linked_tuple.get(333): {linked_tuple.get(333)}") # None

class Dict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        # 구현해보세요!
        self.items[hash(key) % len(self.items)].add(key, value)
    
    def get(self, key):
        # 구현해보세요!
        return self.items[hash(key) % len(self.items)].get(key)

my_dict = Dict()
my_dict.put("test", 3)
for i in range(1, 12):
    my_dict.put(str(i), i)
for i in range(1, 12):
    print(my_dict.get(str(i)))
print(my_dict.get("test"))  # 3이 반환되어야 합니다!