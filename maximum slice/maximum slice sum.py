def solution(A):
    max_sum = 0
    max_slice_sum = 0
    if len(A) <= 2:
        return sum(A)
    for a in A:
        max_sum = max(0, max_sum + a)
        max_slice_sum = max(max_slice_sum, max_sum)
    return max_slice_sum



def solution(A):  ###this is wrong
    result =0
    max=-2147483648
    for i in xrange(0,len(A)):
        if A[i]<0:
            result+=A[i]
            if max<result:
                max=result
            if result<0:
                result=0
        elif A[i]==0:
            if max<result:
                max=result
            continue
        else:
            while i<len(A) and A[i]>0:
                result =+A[i]
            if max<result:
                max=result
                i-=1
    return max