def solution(A):
    sumA = sum(A)
    num_of_pairs = 0
    for i in range(len(A) - 1):
        if A[i] == 0:
            num_of_pairs += sumA
        else:
            sumA -= 1
        if num_of_pairs > 1000000000:
            num_of_pairs = -1
            break
    return num_of_pairs
