# My first attempt using stack.
# But as I didn't take the closing bracket means an ending into account.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if self.isParenthses(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        return not stack

    def isParenthses(self, x: str, y: str) -> bool:
        return (x == '(' and y == ')') or (x == '[' and y == ']') or (x == '{' and y == '}')


# So this time, if the character is an closing bracket, we can end the calculation earlier.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
