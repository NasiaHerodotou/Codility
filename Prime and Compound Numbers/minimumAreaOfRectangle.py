import sys


def solution(N):
    i = 1
    minArea = sys.maxint
    while (i * i <= N):
        if (N % i == 0):
            A = i
            B = N / i
            area = 2 * (A + B)
            minArea = min(area, minArea)
        i += 1
    return minArea
