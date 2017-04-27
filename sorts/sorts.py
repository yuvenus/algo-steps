# sorts
# Venus Yu
import random

def rand_quick (A, p, r):
    if p < r:
        partTuple = rand_part(A, p, r)
        rand_quick(A, p, partTuple[0] - 1)
        rand_quick(A, partTuple[1] + 1, r)

def rand_part (A, p, r):
    i = random.randint(p, r)
    exchange(A, r, i)
    return partition(A, p, r)

def partition (A, p, r):
    pivot = A[r]
    i = p
    ##number of copies of the pivot
    c = 1
    j = p
    while j <= r - c:
        if A[j] == pivot:
            exchange(A, r - c, j)
            c += 1
        else:
            if A[j] < pivot:
                exchange(A, i, j)
                i += 1
            j += 1
    for j in range (0, c):
        exchange(A, i+j, r - c + 1 + j)
    return i, i + c - 1

def exchange (A, n1, n2):
    temp = A[n1]
    A[n1] = A[n2]
    A[n2] = temp

def check_sort(A):
    sort = True
    i = 0
    while sort and i < len(A) - 1:
        if A[i] > A[i + 1]:
            sort = False;
        else:
            i += 1
    return sort

def check_rev_sort(A):
    rev = True
    i = 0
    while rev and i < len(A) - 1:
        if A[i] <= A[i + 1]:
            rev = False
        else:
            i += 1
    return rev

def fix_rev_sort(A):
    sub = 1
    for i in range(0, len(A)/2):
        j = len(A) - (i + sub)
        hold = A[i]
        A[i] = A[j]
        A[j] = hold

# 1. Read input list.
n = int(raw_input())

A = range(n)

for i in range(n):
    A[i] = int(raw_input())

# 2. Baseline sort.

if check_sort(A) == False:
    if (check_rev_sort(A) == True):
        fix_rev_sort(A)
    else:
        rand_quick(A,0,len(A) - 1);

# 3. Write output list.
for x in A:
    print x
