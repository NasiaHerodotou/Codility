# def solution(N, A):
#     counters = [0] * N
#     for item in A:
#         if item >= 1 and item <= N:
#             counters[item - 1] += 1
#         else:
#             maxCounter = max(counters)
#             for i in range(0, N):
#                 counters[i] = maxCounter
#     return counters



def solution(N, A):
    counters = [0] * N
    m = 0
    last = 0
    for op in A:
        op -= 1  # 1-based indexing, fucking really?
        if op == N:
            last = m
            continue
        counters[op] = max(counters[op], last) + 1
        m = max(m, counters[op])
    for i in xrange(N):
        counters[i] = max(counters[i], last)
    return counters
