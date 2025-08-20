package _2nd_week_java;

public abstract class _02_16_get_count_of_ways_to_target_by_doing_plus_or_minus {
    public static void main(String[] args) {
        int[] numbers = new int[]{1, 1, 1, 1, 1};
        int target_number = 3;
        System.out.println(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number));
    }

    public static int get_count_of_ways_to_target_by_doing_plus_or_minus(int[] array, int target) {
        count_of_ways_to_target_recursively(array, target, 0, 0);
        return count[0];
    }

    public static int[] count = new int[]{0};
    public static void count_of_ways_to_target_recursively(int[] array, int target, int index, int currentSum) {
        if (index == array.length) {
            if (currentSum == target) {
                count[0]++;
            }
            return;
        }
        count_of_ways_to_target_recursively(array, target, index + 1, array[index] + currentSum);
        count_of_ways_to_target_recursively(array, target, index + 1, -array[index] + currentSum);
    }
}
