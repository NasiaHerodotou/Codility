# We can use Kadane’s algorithm from two directions. First, we can safely ignore A[0] and A[N-1] since by definition
# they can’t be a part of any double-slice sum.
#
# Now, define K1[i] as the maximum sum contiguous subsequence ending at index ii, and similarly, define  K2[i] as the
#  maximum sum contiguous subsequence starting with index ii.
#
# Then, iterate over ii, and find the maximum sum of K1[i-1]+K2[i+1]. This is the max double slice sum.


def solution(A):
    n = len(A);
    K1 = [0] * n
    K2 = [0] * n
    for i in xrange(1, n - 1):
        K1[i] = max(K1[i - 1] + A[i], 0)
    for i in xrange(n - 2, 1, -1):
        K2[i] = max(K2[i + 1] + A[i], 0)
    maximum = 0
    for i in xrange(1, n - 1):
        maximum = max(maximum, K1[i - 1] + K2[i + 1])
    return maximum
