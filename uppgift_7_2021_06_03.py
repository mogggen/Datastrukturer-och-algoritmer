from math import ceil
from random import getrandbits

arr = ['good', 'good', 'good', 'good', 'bad', 'good', 'good', 'bad', 'good', 'good', 'bad', 'bad']
def OR(subarr, l, r):
    return "bad" in subarr[l:r]

print("O(k (log n - log k)")

# print(OR(["good", "bad", "good"], 4, 3))

#arr = ["good" if not not getrandbits(1) else "bad" for _ in range(12)]

#print(arr)



# binary search alternating left and right, when the OR operator returns false:
#   discard them from the search range, and offset the indices
# if you reach length one and the OR is still True:
#   add the bad index to found_bads
# repeat until arr is empty

def F(A, l, r):
    i = int( ceil( (l+r) / 2 ) )
    for _ in A[1:-1]:
        if _ == A[i]:
            print("i", sep='', end="")
        if _ == A[l]:
            print("l", sep='', end="")
        if _ == A[r]:
            print("r", sep='', end="")
        
        print('\t', _ sep='')

    input()

    if OR(arr, l, r)
        return F(A, i+1, r)

F(arr, 0, len(arr) - 1)
