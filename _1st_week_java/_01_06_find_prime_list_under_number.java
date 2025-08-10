/*
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 

소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
[2, 3, 5, 7, 11, 13, 17, 19]
 */

import java.util.ArrayList;
import java.util.List;

public class _01_06_find_prime_list_under_number extends TempleteUtils {
    public static void main(String[] args) {
        int input = 20;

        print(find_prime_list_under_number(input));
    }

    public static int[] find_prime_list_under_number(int number) {
        List<Integer> primes = new ArrayList<>();
        for (int i=2; i<=number; i++) {
            boolean isPrime = true;
            for (int prime : primes) {
                if (prime * prime <= i && i % prime == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(i);
            }
        }
        return primes.stream().mapToInt(i -> i).toArray();
    }
}


