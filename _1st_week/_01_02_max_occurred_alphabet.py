def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = find_alphabet_occurrence_array(string) 
    print("alphabet_occurrence_array =", alphabet_occurrence_array)
    index = 0
    max_count = alphabet_occurrence_array[0]
    for i in range(len(alphabet_occurrence_array)):
        if max_count < alphabet_occurrence_array[i]:
            index = i
            print("index =", index)
            max_count = alphabet_occurrence_array[i]
    return chr(index + ord('a'))

def find_alphabet_occurrence_array(string):
    alphabet_count = [0] * 26
    string = string.lower()
    for alphabet in string:
        if not alphabet.isalpha():
            continue
        # print("alphabet =", alphabet)
        index = ord(alphabet) - ord('a')
        # print("index =", index)
        alphabet_count[index] += 1
    return alphabet_count


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))