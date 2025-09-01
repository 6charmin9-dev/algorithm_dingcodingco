package _3rd_week_java;

import java.util.Stack;

/*
Q2. ✍️ 올바른 괄호
Q. 문제 설명
Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

()() 또는 (())() 는 올바르다.
)()( 또는 (()( 는 올바르지 않다.

이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.
"(())()" # True
"(((("   # False
 */
public class _03_13_is_correct_parenthesis {
    public static void main(String[] args) {
        System.out.println("정답 = true / 현재 풀이 값 = " + isCorrectParenthesis("(())"));
        System.out.println("정답 = false / 현재 풀이 값 = " + isCorrectParenthesis(")"));
        System.out.println("정답 = false / 현재 풀이 값 = " + isCorrectParenthesis("((())))"));
        System.out.println("정답 = false / 현재 풀이 값 = " + isCorrectParenthesis("())()"));
        System.out.println("정답 = false / 현재 풀이 값 = " + isCorrectParenthesis("((())"));
    }

    public static boolean isCorrectParenthesis(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
