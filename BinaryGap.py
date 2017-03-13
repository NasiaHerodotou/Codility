
def solution(N):
    gap = 0
    maxGap = 0
    for bit in str(bin(N))[2:]:
        if bit == "0":
            gap += 1
        else:
            if gap > maxGap:
                maxGap = gap
            gap = 0
    return maxGap

