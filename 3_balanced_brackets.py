s = "(])"


def isValid(s: str) -> bool:
    # if you see something like this problem - think stack

    # Initialize a stack to track open parenthesis
    stack = []
    # Create a hashtable of open and closing brackets
    open_brackets = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    close_brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    # Move through the string input
    # For each character of the string
    for char in s:
        # If the character is an open bracket
        if char in open_brackets:
            # Append it to the stack
            stack.append(char)
        # If it is a closing bracket
        elif char in close_brackets:
            # and the stack is empty
            if len(stack) == 0:
                # string is not balance, return false
                return False
            # Otherwise Compare it with the item
            # at the top of the stack
            # If it matches the corresponding opening bracket
            elif stack[-1] == close_brackets[char]:
                # Pop the opening bracket from the stack
                stack.pop()
            # If it doesn't
            else:
                # return False
                return False
    # Return if the stack is empty or not
    return len(stack) == 0


print(isValid(s))
