# def solution(N):
#     count = 1
#     for i in range(N, 1, -1):
#         if (N / float(i)).is_integer():
#             count += 1
#     return count


def solution(n):
    i = 1
    result = 0
    while (i * i < n):
        if (n % i == 0): #akrivis diairesi
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    return result
