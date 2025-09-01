package _3rd_week_java;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Stream;

/*
Q1. ✍️ 쓱 최대로 할인 적용하기
Q. 
다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 
하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다. 
쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 
이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
[30000, 2000, 1500000] # 상품의 가격
[20, 40]               # 쿠폰, 할인율의 단위는 % 입니다.
 */
public class _03_12_get_max_discounted_price {
    public static void main(String[] args) {
        // int[] shop_prices = {30000, 2000, 1500000};
        // int[] user_coupons = {20, 40};
        
        System.out.println("정답 = 926000 / 현재 풀이 값 = " + 
            getMaxDiscountedPrice(new int[]{30000, 2000, 1500000}, new int[]{20, 40}));
        
        System.out.println("정답 = 485000 / 현재 풀이 값 = " + 
            getMaxDiscountedPrice(new int[]{50000, 1500000}, new int[]{10, 70, 30, 20}));
        
        System.out.println("정답 = 1550000 / 현재 풀이 값 = " + 
            getMaxDiscountedPrice(new int[]{50000, 1500000}, new int[]{}));
        
        System.out.println("정답 = 1458000 / 현재 풀이 값 = " + 
            getMaxDiscountedPrice(new int[]{20000, 100000, 1500000}, new int[]{10, 10, 10}));
    }

    public static int getMaxDiscountedPrice(int[] shop_prices, int[] user_coupons) {
        Integer[] pricesBoxed = Arrays.stream(shop_prices).boxed().toArray(Integer[]::new);
        Integer[] couponsBoxed = Arrays.stream(user_coupons).boxed().toArray(Integer[]::new);
        Arrays.sort(pricesBoxed, Comparator.reverseOrder());
        Arrays.sort(couponsBoxed, Comparator.reverseOrder());
        int maxDiscountedPrice = 0;
        int price_idx = 0;
        while (price_idx < pricesBoxed.length && price_idx < couponsBoxed.length) {
            maxDiscountedPrice += pricesBoxed[price_idx] * (100 - couponsBoxed[price_idx]) / 100;
            price_idx++;
        }
        while (price_idx < pricesBoxed.length) {
            maxDiscountedPrice += pricesBoxed[price_idx];
            price_idx++;
        }
        return maxDiscountedPrice;
    }
}
