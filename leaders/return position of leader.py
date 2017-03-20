def solution(A):
    n = len(A)
    positions = []
    size = 0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            count += 1
            positions.append(k)
    if count > n // 2:
        leader = candidate
    else:
        return -1
    return positions[0]