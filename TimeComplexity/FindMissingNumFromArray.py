# solution([1,4,2,5])
# solution([1,3,6,5,4])
# solution([0])
# solution([1,3])
# solution([1])
# solution([2,3,4,5])
# solution([1,2,3,4])

# def solution(A):
#     if len(A) == 0:
#         return 0
#     elif len(A) == 1:
#         return A[0]
#     else:
#         if (0 in A) == True:
#             return 0
#         elif (1 in A) == False:
#             return 1
#         else:
#             sortedA = sorted(A)
#             for i in range(len(sortedA) - 1):
#                 if sortedA[i + 1] - sortedA[i] != 1:
#                     return sortedA[i] + 1
#                     break
#             return sortedA[len(sortedA) - 1] + 1


def solution(A):
    xor = len(A) + 1
    for a, i in enumerate(A, 1):
        xor = xor ^ a ^ i
    return xor