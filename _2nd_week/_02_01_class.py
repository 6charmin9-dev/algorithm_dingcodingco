class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

person_1 = Person("홍길동")
person_1.greet()

person_2 = Person("이몽룡")
person_2.greet()
