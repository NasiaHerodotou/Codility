

def solution(X, Y, D):
    mod = ((Y - X) % D)
    jumps = (Y - X) / D
    if mod == 0:
        return jumps
    else:
        return jumps+1

