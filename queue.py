from collections import deque


q = deque()
for i in range(int(input())):
    o = list(map(int, input().split()))
    if o[0] == 1:
        q.append(o[1])
    if o[0] == 2:
        q.popleft()
    if o[0] == 3:
        print(q[0])
