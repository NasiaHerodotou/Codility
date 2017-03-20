# def solution(A):
#     max_profit = 0
#     for i in xrange(0, len(A) - 1):
#         for j in xrange(i + 1, len(A)):
#             max_profit = max(max_profit, A[j] - A[i])
#     return max_profit


def solution(A):
    max_profit = max_slice = 0
    for i in xrange(1, len(A)):
        max_profit = max(0, max_profit + (A[i] - A[i - 1]))
        max_slice = max(max_slice, max_profit)
    if max_slice > 0:
        return max_slice
    else:
        return 0
