class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in dict:
                stack.append(i)
            elif len(stack) == 0 or dict[stack.pop()] != i:
                return False
        return len(stack) == 0
            