input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for num in range(2, number + 1): #N
        for prime in prime_list: #N [2, 3, 5, 7, 11, 13, 17, 19]
            if prime * prime <= num and num % prime == 0: # 소수가 아닌 조건
                break
        else:
            prime_list.append(num)
    return prime_list



result = find_prime_list_under_number(input)
print(result)

# 시간복잡도: O(N^2) -> O(Nroot(N))
# 공간복잡도: O(N)