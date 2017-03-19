# def solution(A):
#     listA = []
#     listB = []
#     count = 0
#     for i in xrange(0, len(A)):
#         listA = range(i - A[i], i + A[i] + 1) #lista me tis times apo pou pianei olos o kiklos me tin aktina tou
#         for j in xrange(i + 1, len(A)):
#             if i != j:
#                 listB = range(j - A[j], j + A[j] + 1) #lista me tis times pou pianei o defteros kiklos me tin aktina
#                 setA = set(listA)
#                 setB = set(listB)
#                 if bool(setA & setB): #o tropos na deis an dio listes ehoun koina simeia
#                     count += 1
#     if count > 10000000:
#         count = -1
#     return count


def solution(A):
    upper = sorted([i + val for i, val in enumerate(A)])
    lower = sorted([i - val for i, val in enumerate(A)])

    counter = 0
    j = 0
    for i, uval in enumerate(upper):
        while j < len(upper) and uval >= lower[j]:
            counter += j - i
            j += 1
        if counter > 10 ** 7:
            return -1

    return counter
