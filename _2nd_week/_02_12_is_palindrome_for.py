input = "abcba"

def is_palindrome2(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 -i]:
            return False
    return True

def is_palindrome(string):
    min_index = 0
    max_index = len(string) - 1
    while min_index < max_index:
        if string[min_index] != string[max_index]:
            return False
        min_index += 1
        max_index -= 1
    return True


print(is_palindrome2(input)) # True