class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        if self.items[index] is None:
            self.items[index] = [(key, value)]
        else:
            self.items[index].append((key, value)) #  체이닝(Chaining): 충돌 해결을 위해 리스트에 추가 # 주소 개방법(address opening): 충돌 해결을 위해 다음 주소값에 값이 있는지 체크하여 없는 주소값에 저장

    def get(self, key):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        if self.items[index] is not None:
            for k, v in self.items[index]:
                if k == key:
                    return v
        return None


my_dict = Dict()
my_dict.put("test", 3)
for i in range(1, 12):
    my_dict.put(str(i), i)
for i in range(1, 12):
    print(my_dict.get(str(i)))
print(my_dict.get("test"))  # 3이 반환되어야 합니다!