package _2nd_week_java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class _02_15_is_available_to_order {
    public static void main(String[] args) {
        String[] menus = {"만두", "떡볶이", "오뎅", "사이다", "콜라"};
        // String[] orders = {"오뎅", "콜라", "만두"};
        String[] orders = {"오뎅", "콜라", "만두", "순대"};
        boolean result = is_available_to_order2(menus, orders);
        System.out.println(result);
    }  
    
    public static boolean is_available_to_order(String[] menus, String[] orders) {
        Set<String> menusSet = new HashSet<>(Arrays.asList(menus));
        boolean result = true;
        for (String order : orders) {
            if (!menusSet.contains(order)) {
                result = false;
                break;
            }
        }
        return result;
    }

    public static boolean is_available_to_order2(String[] menus, String[] orders) {
        Arrays.sort(menus);
        for (String order : orders) {
            if (!binarySearch(menus, order)) {
                return false;
            }
        }
        return true;
    }

    public static boolean binarySearch(String[] array, String target) {
        int low = 0;
        int high = array.length - 1;
        int middle = (low + high) / 2;
        while (low <= high) {
            if (target.compareTo(array[middle]) > 0) {
                low = middle + 1;
            } else if (target.compareTo(array[middle]) < 0) {
                high = middle - 1;
            } else {
                return true;
            }
            middle = (low + high) / 2;
        }
        return false;
    }
}
