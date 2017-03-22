# def solution(N, M):
#     counter = 0
#     x = 0
#     eaten = []
#     while x not in eaten:
#         print x
#         eaten.append(x)
#         x = (x + M) % N
#         counter += 1
#     return counter


def solution(N, M):
    x = 0
    while x != 1:
        x = N
        y = M
        while y != 0:
            (x, y) = (y, x % y)
        N = N / x
        M = M / x
    return N
