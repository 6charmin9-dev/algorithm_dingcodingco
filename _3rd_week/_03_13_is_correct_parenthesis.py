'''
Q2. ✍️ 올바른 괄호
Q. 문제 설명
Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

()() 또는 (())() 는 올바르다.
)()( 또는 (()( 는 올바르지 않다.

이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.
"(())()" # True
"(((("   # False
'''
def is_correct_parenthesis_1(string):
    # 구현해보세요!
    if len(string) == 0:
        return True
    if string[0] == ')':
        return False
    stack = [string[0]]
    for parenthesis in string[1:]:
        if stack and stack[-1] != parenthesis:
            stack.pop()
        else:
            stack.append(parenthesis)
    return not stack

def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []
    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        else:
            if not stack:
                return False
            stack.pop()
    # print(f"stack: {stack}")
    return not stack # stack 이 비어 있으면 True, 비어 있지 않으면 False



print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))