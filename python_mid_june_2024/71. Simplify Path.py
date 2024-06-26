class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = deque()

        for d in dirs:
            if d == '' or d == '.':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        res = '/' + '/'.join(stack)
        return res
