from collections import deque

size, rot = map(int, input().split())
arr = deque(map(int, input().split()))

arr.rotate(-rot)
for i in arr:
    print(i, end= ' ')