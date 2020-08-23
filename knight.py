n = int(input())

memo_knight = {}

def knight(i, j, n):
    possible_moves = ((i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i), (j, -i), (-j, -i))
    visited = {(0, 0)}
    paths = {(0, 0)}
    level = 0
    while(len(paths)):
        level += 1
        cur_level = set(paths)
        paths.clear()
        for x, y in cur_level:
            for ii, jj in possible_moves:
                if (x + ii, y + jj) == (n-1, n-1):
                    memo_knight[(i, j, n)] = memo_knight[(j, i, n)] = level 
                    return level 
                if x + ii < n and y + jj < n and x + ii >= 0 and y + jj >= 0 and (x + ii, y + jj) not in visited:
                    paths.add((x + ii, y + jj))
                    visited.add((x + ii, y + jj))
    memo_knight[(i, j, n)] = memo_knight[(j, i, n)] = -1
    return -1


for i in range(1, n):
    for j in range(1, n):
        #print(memo_knight)
        if (i, j, n) in memo_knight:
            print(memo_knight[(i, j, n)], end=' ')
        else:
            print(knight(i, j, n), end=' ')
    print()


                
