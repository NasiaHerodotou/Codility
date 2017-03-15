# def solution(A, B, K):
#     sum = 0
#     intRange = range(A, B + 1)
#     for integer in intRange:
#         if integer % K == 0:
#             sum += 1
#     return sum


def solution(A, B, K):
    sum1 = (A - 1) / K
    sum2 = B / K
    return sum2 - sum1
