def factorial(n):
    # 이 부분을 채워보세요!
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5)) # 120