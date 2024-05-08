def max(a, b):
    return a if a >= b else b

def solve():
    n, m, r, c = map(int, input().split())
    print(max(n - r, r - 1) + max(m - c, c - 1))

if __name__ == "__main__":
    solve()
