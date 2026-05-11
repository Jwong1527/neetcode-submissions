class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize stack

        if len(s) % 2 != 0:
            return False  

        for character in s:
            if character in "({[":
                stack.append(character)  # Push opening bracket
            elif character == ")" and stack and stack[-1] == "(":
                stack.pop()  # Pop matching opening bracket
            elif character == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif character == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False #If we never see an opening brace then it can't be valid. 

        return not stack  # Return True if stack is empty, else False