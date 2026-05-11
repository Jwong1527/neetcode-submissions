class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0: return False

        stack = []

        for character in s:
            if character in "([{":
                stack.append(character)
            elif character == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif character == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif character == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False 
        
        return not stack 
            
