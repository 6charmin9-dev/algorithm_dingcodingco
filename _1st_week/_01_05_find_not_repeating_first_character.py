input = "abadabac"

def find_not_repeating_first_character(string):
    char_to_repeating_cnt = {} #,N * 2
    for char in string: #N
        char_to_repeating_cnt[char] = char_to_repeating_cnt.get(char, 0) + 1
    for entry in char_to_repeating_cnt.items(): #N
        if entry[1] == 1:
            return entry[0]
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

# 시간복잡도: O(N)
# 공간복잡도: O(N)