def solution(N, P, Q):
    from math import sqrt

    # Find out all the primes with Sieve of Eratosthenes
    prime_table = [False] * 2 + [True] * (N - 1)
    prime = []
    prime_count = 0
    for element in xrange(2, int(sqrt(N)) + 1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    for element in xrange(int(sqrt(N)) + 1, N + 1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1

    # Compute the semiprimes information
    semiprime = [0] * (N + 1)
    # Find out all the semiprimes.
    # semiprime[i] == 1 when i is semiprime, or
    #                 0 when i is not semiprime.
    for index_former in xrange(prime_count - 1):
        for index_latter in xrange(index_former, prime_count):
            if prime[index_former] * prime[index_latter] > N:
                # So large that no need to record them
                break
            semiprime[prime[index_former] * prime[index_latter]] = 1
    # Compute the number of semiprimes until each position.
    # semiprime[i] == k means:
    # in the range (0,i] there are k semiprimes.
    for index in xrange(1, N + 1):
        semiprime[index] += semiprime[index - 1]

    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1]
    question_len = len(P)
    result = [0] * question_len
    for index in xrange(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index] - 1]

    return result

#
# def solution(N, P, Q):
#     result = []
#     primes = sieve(N)
#     print "primes=", primes
#     semiprimes = []
#     for i in xrange(0, N):
#         for j in xrange(0, N):
#             if primes[i] * primes[j] != 0:
#                 if (i * j) <= N:
#                     semiprimes.append(i * j)
#     setSemi = set(semiprimes)
#     semis = list(setSemi)
#     print semis
#     for iter in xrange(0, len(P)):
#         count = 0
#         for semi in semis:
#             if semi <= Q[iter] and semi >= P[iter]:
#                 count += 1
#         result.append(count)
#     return result
#
#
# def sieve(n):
#     sieve = [1] * (n + 1)
#     sieve[0] = sieve[1] = 0
#     i = 2
#     while (i * i <= n):
#         if (sieve[i]):
#             k = i * i
#             while (k <= n):
#                 sieve[k] = 0
#                 k += i
#         i += 1
#     return sieve
