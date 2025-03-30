


def split(paren):
    res = []
    score = 0
    start = 0
    end = 0
    for i in range(len(paren)):
        if paren[i] == "(":
            score +=1
            if score > 1:
                start = start1 # in order to not override the initial position
            else:
                start1 = i  # in order to save the initial position
                start = start1 # in order to not override the initial position
        elif paren[i] == ")":
            score -= 1
            end = i
        if score == 0:
            a = paren[start:end+1]
            res.append(a)
        elif score < 0:
            return None

    return res


##print(split("((()))(())()()(()())"))
##print(split("((())())(()(()()))"))
##print(split("()()(())"))
##print(split("(()(()()))()(((()))()(()))(()((()))(())())"))