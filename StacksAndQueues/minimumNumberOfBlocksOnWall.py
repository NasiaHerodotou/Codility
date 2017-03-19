def solution(H):
    count = 0
    stack = []
    for i in range(0, len(H)):
        while stack != [] and stack[-1] > H[i]:
            stack.pop()
        if stack == [] or stack[-1] < H[i]:
            stack.append(H[i])
            count += 1
    return count
