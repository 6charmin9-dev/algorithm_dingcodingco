input = 20
# input = 100 # 너무 오래걸려서 답이 안나온다. 

'''
Q. 피보나치 수열의 20번째 수를 구하시오.
'''
def fibo_recursion(n):
    # 구현해보세요!
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765