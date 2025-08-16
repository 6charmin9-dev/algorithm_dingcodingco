# BOJ 1158

def josephus_problem(n, k):
   # 이 부분을 채워보세요!
    people = list(range(1, n + 1))
    relocated_people = []
    i = 0
    while len(people) != 0:
        i = (i - 1 + k) % len(people)
        relocated_people.append(people.pop(i))

    print("<" + ", ".join(map(str, relocated_people)) + ">")

# 입력 예시: 7 3
# 출력 예시: <3, 6, 2, 7, 5, 1, 4>

# people = 1, 2, 3, 4, 5, 6, 7 / i = 2
# people = 1, 2, 4, 5, 6, 7 / i = 4
# people = 1, 2, 4, 5, 7 / i = 1 
# people = 1, 4, 5, 7 / i = 3
# people = 1, 4, 5 / i = 2

n, k = map(int, input().split())
josephus_problem(n, k)

