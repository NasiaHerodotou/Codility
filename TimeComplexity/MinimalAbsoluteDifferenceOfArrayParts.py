def solution(A):
    sum2 = sum(A)
    min_diff = None
    sum1 = 0
    for i in xrange(1, len(A)):
        sum1 += A[i - 1]
        sum2 -= A[i - 1]
        diff = abs(sum1 - sum2)

        if min_diff is None:
            min_diff = diff
        else:
            min_diff = min(min_diff, diff)
    return min_diff
