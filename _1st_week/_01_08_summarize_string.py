def summarize_string(input_str):
    alphabet_to_occurrence_cnt = {}
    for alphabet in input_str:
        alphabet_to_occurrence_cnt[alphabet] = alphabet_to_occurrence_cnt.get(alphabet, 0) + 1
        # print(f"alphabet = {alphabet}, count = {alphabet_to_occurrence_cnt[alphabet]}")
    result = ""
    for entry in alphabet_to_occurrence_cnt.items():
        if len(result) != 0:
            result.append("/")
        # print(f"entry = {entry}")
        result.append(f"{entry[0]}{entry[1]}") # O(N^2)
    return result

# 시간복잡도: O(N)
# 공간복잡도: O(1)


def summarize_string2(target_string):
    # 이 부분을 채워보세요!
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str

input_str = "acccdeee"

print(summarize_string2(input_str)) #a1/c3/d1/e3