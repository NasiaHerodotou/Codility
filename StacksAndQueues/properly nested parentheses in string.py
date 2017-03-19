def solution(S):
    opening = []
    if len(S) == 0:
        return 0
    for s in S:
        if s == "(":
            opening.append(s)
        else:
            if len(opening) == 0:
                return 0
            else:
                opening.pop()
    if len(opening) != 0:
        return 0
    else:
        return 1
