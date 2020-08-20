#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    s = [sum(h1), sum(h2), sum(h3)]
    while not (s[0] == s[1] == s[2]):
        o = s.index(max(s[0], s[1], s[2]))
        if o == 0:
            k = h1.pop(0)
            s[0] = s[0] - k
        if o == 1:
            k = h2.pop(0)
            s[1] = s[1] - k
        if o == 2:
            k = h3.pop(0)
            s[2] = s[2] - k
        
    
    return s[0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
