class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ('(', '{', '['):
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                previous_character = stack.pop(-1)
                if character == ')' and previous_character != '(':
                    return False
                elif character == '}' and previous_character != '{':
                    return False
                elif character == ']' and previous_character != '[':
                    return False
        if len(stack) != 0:
            return False
        return True
