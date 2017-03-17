# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    if len(A) == 0:
        count = 0
    else:
        count = 1
    A = sorted(A)
    for i in xrange(0, len(A) - 1):
        if A[i] != A[i + 1]:
            count += 1
    return count
