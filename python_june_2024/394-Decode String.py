class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                subs = ""
                while stack and stack[-1] != '[':
                    subs = stack.pop() + subs
                if stack and stack[-1] == '[':
                    stack.pop()
                    i = 1
                    k = 0
                    while stack and stack[-1].isdigit():
                        k = int(stack.pop())*i + k
                        i *= 10
                    subs *= k
                    stack.append(subs)

            else:
                stack.append(char)
        
        return ''.join(stack)