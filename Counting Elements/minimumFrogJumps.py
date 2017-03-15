# def solution(X, A):
#     for i in range(0, len(A)):
#         if set(A[:i + 1]) == set(range(1, X + 1)):
#             return i
#     return -1


def solution(X, A):
    count = [False] * X
    sum = 0
    for i in range(len(A)):
        if not (count[A[i] - 1]):
            count[A[i] - 1] = True
            sum += 1
        if sum == X:
            return i
    return -1
