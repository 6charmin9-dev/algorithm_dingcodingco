# input = 50
input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

'''
Q. 피보나치 수열의 100번째 수를 구하시오.
'''
def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    # print(n, fibo_memo)
    if n not in fibo_memo:
        fibo_memo[n] = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    return fibo_memo[n]


print(fibo_dynamic_programming(input, memo)) # 50 -> 12586269025
print(fibo_dynamic_programming(input, memo)) # 100 -> 354224848179261915075