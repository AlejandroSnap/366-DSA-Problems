from collections import deque

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    rest = 0
    for p in s:
        if p == '(':
            rest += 1
        elif rest - 1 == 0 and p == ')':
            ans += 2
            rest = 0

    return ans

s = "(()"
print(longestValidParentheses(s))

s = ")()())"
print(longestValidParentheses(s))

s = "()(())"
print(longestValidParentheses(s))
