# def solution(A):
#     for p in xrange(0, len(A)):
#         for q in xrange(p + 1, len(A)):
#             for r in xrange(q + 1, len(A)):
#                 if A[p] + A[q] > A[r] and A[q] + A[r] > A[p] and A[r] + A[p] > A[q]:
#                     return 1
#     return 0


def solution(A):
    A = sorted(A)
    a = b = c = 0
    for i in reversed(A):
        a, b, c = i, a, b
        if a + b > c and a + c > b and c + b > a:
            return 1
    else:
        return 0
