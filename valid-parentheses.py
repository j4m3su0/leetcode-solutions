class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char == ")":
                if len(stack) > 0:
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            elif char == "}":
                if len(stack) > 0:
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            elif char == "]":
                if len(stack) > 0:
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
