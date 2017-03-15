# def solution(A):
#     setSortedA = set(sorted(A))
#     listSet = list(setSortedA)
#     for i in range(1,len(listSet)+1):
#         if listSet[i-1] != i:
#             return i
#     return len(listSet)+1


def solution(A):
    A = set(sorted(A))
    m = set(range(1, len(A) + 1))
    x = m - A  # returns A SET with all the values that are in m but not in A
    return min(x) if x else len(A) + 1
