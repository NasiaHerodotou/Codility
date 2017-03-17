# def solution(S, P, Q):
#     M = len(P)
#     dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
#     minimum_factor_list = [0] * M
#     for i in range(0, M):
#         min_factor = 100000000
#         start = P[i]
#         end = Q[i]
#         seq = S[start:end + 1]
#         for letter in seq:
#             imp_factor = dict[letter]
#             if imp_factor < min_factor:
#                 min_factor = imp_factor
#             minimum_factor_list[i] = min_factor
#     return minimum_factor_list


def solution(S, P, Q):
    M = len(P)
    dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    factors = [0] * len(S)
    minimum_factor_list = [None] * M
    for i in range(0, len(S)):
        factors[i] = dict[S[i]]
    for i in range(0, M):
        minimum_factor_list[i] = min(factors[P[i]:Q[i] + 1])
    return minimum_factor_list
