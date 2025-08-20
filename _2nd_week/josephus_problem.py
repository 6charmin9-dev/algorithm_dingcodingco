# BOJ 1158

'''
# 문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
'''
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

