#### ---Jerry Tarus--- ####


def is_balanced(expression):
    exp = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            exp.append(char)
        elif char in brackets.keys():
            if not exp or exp.pop() != brackets[char]:
                return False

    return not exp

# See if working

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  ### This should be True
print(is_balanced(expression2))  ### And this False



#### ---Jerry Tarus--- ####

