# def solution(A):
#     max = -1000000000
#     for p in xrange(0, len(A)):
#         for q in xrange(p + 1, len(A)):
#             for r in range(q + 1, len(A)):
#                 product = A[p] * A[q] * A[r]
#                 print product
#                 if product > max:
#                     max = product
#     return max


def solution(A):
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])
