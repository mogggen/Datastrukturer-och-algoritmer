from math import inf, ceil
from random import shuffle

A = [-1, 1, 2, 3, 44, 4, 5, 55, 6, -34, -44, 99, 52, 7, 8, 9]


def F(A, l=1, r=len(A)-1):
    i = int( ceil( (l+r) / 2 ) )

    for _ in A[1:-1]:
        if _ == A[i]:
            print(" i", end="")
        if _ == A[l]:
            print(" l", end="")
        if _ == A[r]:
            print(" r ", end="")
        print("\t", end="")
        
        if _ > 0:
            print("+"* _, end="")
        if _ < 0:
            print("-"* abs(_), end="")
        
        print()

    input()
    
    if l == r:
        return A[i]

    if A[i] < A[i+1]:
        return F(A, i+1, r)
    
    if A[i] > A[i+1] and A[i-1] > A[i]:
        return F(A, l, i-1)

    return A[i]


for j in range(50):
    input()
    shuffle(A)

    solution = F( [inf]+A+[inf] )
    print( "solved" )
