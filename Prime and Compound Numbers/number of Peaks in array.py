# def solution(A):
#     divs = []
#     peaks = []
#     maxBlocks = 0
#     for i in xrange(1, len(A) - 1):
#         if A[i] > A[i - 1] and A[i] > A[i + 1]:
#             peaks.append(A[i])
#     divs = factors(len(A))
#     for factor in divs:
#         i = 0
#         truth = []
#         while (i < len(A)):
#             factorArray = A[i:(i + factor)]
#             truth.append(any(x in peaks for x in factorArray))
#             i = i + factor
#         if all(element == True for element in truth):
#             maxBlocks = max(maxBlocks, len(A) / len(factorArray))
#     return maxBlocks
#
#
# def factors(n):
#     A = []
#     i = 1
#     result = 0
#     while (i * i <= n):
#         if (n % i == 0):  # akrivis diairesi
#             A.append(i)
#             A.append(n / i)
#         i += 1
#     return A


def solution(A):
    from math import sqrt

    A_len = len(A)
    peaks_until_here = [0] * A_len

    # Retrieve how many peaks exist from beginning to current
    # position.
    for index in xrange(1, A_len - 1):
        peaks_until_here[index] = peaks_until_here[index - 1]
        if A[index] > A[index - 1] and A[index] > A[index + 1]:
            peaks_until_here[index] += 1
    if A_len < 3 or peaks_until_here[-2] == 0:
        # The array is too short to have a peak. OR
        # There is no peak in this array.
        return 0
    peaks_until_here[-1] = peaks_until_here[-2]

    max_blocks = 0
    # Compute every possible partition plan, and find out the
    # one with most blocks.
    for candidate in xrange(1, int(sqrt(A_len)) + 1, 1):
        if A_len % candidate == 0:
            blocks, block_size = candidate, A_len // candidate

            # Check the first block.
            if peaks_until_here[0] < peaks_until_here[block_size - 1]:
                # Check the following blocks.
                for each_block in xrange(block_size, A_len, block_size):
                    if peaks_until_here[each_block - 1] == peaks_until_here[each_block + block_size - 1]:
                        # No peak is found in the next block
                        # This partition plan is not accepted
                        break
                else:
                    max_blocks = blocks

            if candidate * candidate == A_len:
                # If candidate is equal to sqrt(A_len) exactly,
                # candidate would equal to A_len//candidate.
                continue

            block_size, blocks = candidate, A_len // candidate
            # Check the first block.
            if peaks_until_here[0] < peaks_until_here[block_size - 1]:
                # Check the following blocks.
                for each_block in xrange(block_size, A_len, block_size):
                    if peaks_until_here[each_block - 1] == peaks_until_here[each_block + block_size - 1]:
                        # No peak is found in the next block
                        # This partition plan is not accepted
                        break
                else:
                    return blocks

    return max_blocks




