from functools import cmp_to_key
from collections import deque

def comparator(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    else:
        return 0

arr = deque()
c = 0
n = int(input())

for i in range(n):
    i = input().split()
    if c < n/2:
        arr.append([int(i[0]), '-'])
        c += 1
    else:
        arr.append([int(i[0]), i[1]])

arr = sorted(arr, key=cmp_to_key(comparator))
for i in arr:
    print(i[1], end=' ')