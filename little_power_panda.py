def egcd(A, B):
    if A == 0:
        return (B, 0, 1)
    else:
        g, y, x = egcd(B % A, A)
        return (g, x - (B // A) * y, y)

def inverse_modulo(A, X):
    g, x, y = egcd(A, X)
    return x % X

for _ in range(int(input())):
    A, B, X = map(int, input().split())
    if B < 0:
        print(pow(inverse_modulo(A, X), abs(B),  X))
    else:
        print(pow(A, B,  X))
