def solution(S):
    stack = [] #create a stack
    if len(S) % 2 != 0: #if the string's length is odd it means that something remains unclosed
        return 0
    dict = {'(': ')', '{': '}', '[': ']'}
    for s in S:
        if s in ('(', '{', '['): #if it is opening bracket push in stack
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            else:  #if it is closing bracket pick the last element and see if it closes the bracket we just picked
                last = stack.pop()
                if dict[last] != s:
                    return 0
    if len(stack) != 0:
        return 0
    else:
        return 1

