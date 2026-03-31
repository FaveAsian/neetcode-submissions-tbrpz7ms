class Solution:
    def decodeString(self, s: str) -> str:        
        string_stack = []
        count_stack = []
        context = ""
        k = 0
        for char in s:
            if char.isdigit():
                k = k*10 + int(char)
            elif char == "[":
                string_stack.append(context)
                count_stack.append(k)
                context = ""
                k = 0
            elif char == "]":
                temp = context
                context = string_stack.pop()
                count = count_stack.pop()
                context += temp*count
            else:
                context += char

        return context