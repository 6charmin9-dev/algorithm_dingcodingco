finding_target = 14
#                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,  12, 13, 14, 15
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] 
# size = 8
# size = 4
# size = 2
# size = 1



'''
Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다. 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
'''
def is_existing_target_number_binary2(target, array):
    # 구현해보세요!
    find_count = 0
    current_min = 0
    current_max = len(array)-1
    current_guess = (current_min + current_max) // 2
    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(f"find_count: {find_count}")
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False

def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    find_count = 0
    size = len(array) // 2
    middle_index = size
    while True:
        find_count += 1
        if target > array[middle_index]:
            middle_index += size // 2
        elif target < array[middle_index]:
            middle_index -= size // 2
        else:
            print(f"find_count: {find_count}")
            return True
        size = size // 2
        if (size == 0):
            break
    return False


result = is_existing_target_number_binary2(finding_target, finding_numbers)
print(result)