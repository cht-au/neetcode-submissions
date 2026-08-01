class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
        
        return not stack
        