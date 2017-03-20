# def solution(A):
#     count = 0
#     for i in xrange(1, len(A)):
#         firstHalf = A[:i]
#         secondHalf = A[i:]
#         if goldenLeader(firstHalf) == goldenLeader(secondHalf) and goldenLeader(firstHalf) != -1:
#             count += 1
#     return count
#
#
# def goldenLeader(A):
#     n = len(A)
#     size = 0
#     for k in xrange(n):
#         if (size == 0):
#             size += 1
#             value = A[k]
#         else:
#             if (value != A[k]):
#                 size -= 1
#             else:
#                 size += 1
#     candidate = -1
#     if (size > 0):
#         candidate = value
#     leader = -1
#     count = 0
#     for k in xrange(n):
#         if (A[k] == candidate):
#             count += 1
#     if count > n // 2:
#         leader = candidate
#     return leader

def solution(A):
    n = len(A)
    d = dict()
    lv = lk = None
    for i in xrange(n):
        if A[i] not in d:  # create a dictionary that has how many times a value appears in A
            d[A[i]] = 1
        else:
            d[A[i]] += 1
        if lv < d[A[i]]:
            lv = d[A[i]]
            lk = A[i]
    if lv <= n / 2:
        return 0
    left = 0
    right = lv
    count = 0
    for i in xrange(n):
        if A[i] == lk:
            left += 1
            right -= 1
        if left > (i + 1) / 2 and right > (n - i - 1) / 2:
            count += 1
    return count
