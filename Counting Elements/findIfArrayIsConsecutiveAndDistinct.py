
def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
    sortedA = sorted(A)
    if sortedA[0] != 1:
        return 0
    setA = set(sortedA)
    cond1 = (len(setA) == len(A))
    cond2 = (sortedA[len(sortedA) - 1] - sortedA[0] + 1 == len(sortedA))
    if (cond1 and cond2) is True:
        return 1
    else:
        return 0
