numbers = [1, 1, 1, 1, 1]
target_number = 3

'''
Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
'''
def get_count_of_ways_to_target_by_doing_plus_or_minus2(array, target):
    count = 0
    def get_all_ways_by_doing_plus_or_minus(array, index, curr_sum, target):
        nonlocal count
        if index == len(array):
            if curr_sum == target:
                # print(f"index: {index}, curr_sum: {curr_sum}, target: {target}, count: {count}")
                count += 1
            return
        
        get_all_ways_by_doing_plus_or_minus(array, index + 1, curr_sum + array[index], target)
        get_all_ways_by_doing_plus_or_minus(array, index + 1, curr_sum - array[index], target)

    get_all_ways_by_doing_plus_or_minus(array, 0, 0, target)
    return count


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    list = [array[0], -array[0]]
    for i in range(1, len(array)):
        next_list = []
        for num in list:
            next_list.append(num + array[i])
            next_list.append(num - array[i])
        list = next_list
    count = 0
    for num in list:
        if num == target:
            count += 1
    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus2(numbers, target_number))  # 5를 반환해야 합니다!