def solution(A):
    for element in A:
        count = 0
        for each in A:
            if each == element:
                count += 1
        if count % 2 == 1:
            return element
            break


# if we xor a number with itself odd number of times the result is 0
# if we xor a number with itself even times the result is the number itself
# so if we xor all numbers in the array because all of them occur even times except for one, the one that will stay at the end will be the number that appears odd times
#xor([9,3,9,3,9,7,9])

def xor(A):
    result = 0
    for element in A:
        result = element ^ result
    print result
