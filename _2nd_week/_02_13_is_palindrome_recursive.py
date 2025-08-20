input = "abcba"

def is_palindrome2(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome2(string[1:-1])

def is_palindrome(string):
    if len(string) <= 1:
        return True
    return (string[0] == string[-1]) and is_palindrome(string[1:-1])


print(is_palindrome(input)) # True