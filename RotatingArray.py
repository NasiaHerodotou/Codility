#solution([3,8,9,7,6],3)

# def solution(A, K):
#     oldA = A
#     rotatedA = A
#     for i in range(K):
#         print ("i=", i)
#         for j in range(len(A)-1):
#             print ("j=", j)
#             if j == 0:
#                 value = oldA[len(A)-1]
#                 rotatedA[j] = value
#                 value = oldA[j]
#                 rotatedA[j+1] = value
#             print "rotatedA[j] = ", rotatedA[j]
#             print "oldA[len(A)-1", oldA[len(A)-1]
#             print "rotatedA[j+1]", rotatedA[j+1]
#             print "oldA[j]", oldA[j]
#             print rotatedA
#             print oldA
#         print rotatedA
#         oldA = rotatedA
#         print oldA
#     return rotatedA

def solution(A, K):
    if len(A) == 0:
        return A

    return A[len(A) - (K % len(A)):] + A[:len(A) - (K % len(A))]
