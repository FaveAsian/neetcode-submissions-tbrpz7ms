class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        marker = {"{": "}", "[": "]", "(": ")"}

        for char in s:
            if char in marker:
                stack.append(char)
            else:
                if stack and marker[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        print(stack)
        return True if not stack else False
