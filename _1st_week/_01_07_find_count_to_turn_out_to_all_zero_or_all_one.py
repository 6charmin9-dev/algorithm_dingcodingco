input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    is_zero = False
    zero_area_starts = []
    one_area_starts = []
    for i in range(0, len(string)):
        if not is_zero and string[i] == '0':
            is_zero = True
            zero_area_starts.append(i)
        if is_zero and string[i] == '1':
            is_zero = False
            one_area_starts.append(i)
    return min(len(zero_area_starts), len(one_area_starts))


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 시간복잡도: 
# 공간복잡도: 