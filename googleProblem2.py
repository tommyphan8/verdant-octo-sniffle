# A zero-indexed array A consisting o N integers is given.  An equilibrium index of this array is any 
# integer P such that 0 <= P < N and the usm of lower in dices is equal to the sum of the 
# elements of higher indices,  i.e. A[0] + A[1] ... + A[P-1] = A[P+1] + .. + A[N-2] + A[N-1]

# Sum of zero elements is assumed to be equal to 0. This can h appen if P=0 or if P = N-1
# For example consider the following array A consisting of N = 8 elements:

# A[0] = -1
# A[1] = 3
# A[2] = -4
# A[3] = 5
# A[4] = 1
# A[5] = -6
# A[6] = 2
# A[7] = 1

# P = 1, 3, and 7 are equilibrium index 

def solution(l):
    for x in range(0, len(l)):
        A = 0
        B = 0
        for y in range(0,x):
            A += l[y]    

        for z in range(x+1, len(l)): 
            B += l[z]

        if A == B:
            return(A,B,x)
    return None
testCase = [-1,3,-4,5,1,-6,2,1]

print(solution(testCase))
