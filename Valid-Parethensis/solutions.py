def validParenthesis2(string):
    parenthesis = []


    if len(string) < 2:
        return False


    for i in range(len(string)):
        if string[i] == "(":
            parenthesis.append("(")
        elif string[i] == ")":
            if len(parenthesis) != 0 and parenthesis[len(parenthesis)-1] == "(":
                parenthesis.pop()
            else:
                return False
        elif string[i] == "[":
            parenthesis.append("[")
        elif string[i] == "]":
            if len(parenthesis) != 0 and parenthesis[len(parenthesis)-1] == "[":
                parenthesis.pop()
            else:
                return False

        elif string[i] == "{":
            parenthesis.append("{")
        elif string[i] == "}":
            if len(parenthesis) != 0 and parenthesis[len(parenthesis)-1] == "{":
                parenthesis.pop()
            else:
                return False

    if len(parenthesis) == 0:
        return True
    else:
        return False


# s = "({{[()]}})"
# print(validParenthesis2(s))