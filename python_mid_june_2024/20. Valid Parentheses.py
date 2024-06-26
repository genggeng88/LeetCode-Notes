class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == ')' or c ==']' or c =='}':
                if not stack:
                    return False
                cpop = stack.pop()
                if c == ')' and cpop != '(':
                    return False
                if c == ']' and cpop != '[':
                    return False
                if c == '}' and cpop != '{':
                    return False
            else:
                stack.append(c)
        
        return not stack