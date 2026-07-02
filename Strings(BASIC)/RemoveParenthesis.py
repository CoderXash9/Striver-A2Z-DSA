class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0

        for char in s:
            if char == "(":
                if opened > 0:
                    result.append(char)
                opened += 1
            else:  # char == ')'
                opened -= 1
                if opened > 0:
                    result.append(char)

        return "".join(result)


"""This solution uses a variable opened to keep track of the current nesting depth (the number of unmatched opening parentheses '('). We traverse the string character by character. When we encounter '(', we first check if opened > 0. If it is, this parenthesis is not the outermost one, so we add it to the result. Then we increment opened because a new parenthesis has been opened. When we encounter ')', we first decrement opened since one parenthesis is being closed. After decrementing, if opened > 0, it means this closing parenthesis is still inside the primitive string, so we add it to the result. If opened becomes 0, it means we have reached the outermost closing parenthesis, so we skip it. Finally, we use "".join(result) to convert the list of characters into a string and return the answer. This approach removes only the outermost parentheses of every primitive valid parentheses string in O(n) time and O(n) space."""
