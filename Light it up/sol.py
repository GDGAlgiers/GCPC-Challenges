n = int(input())

if n:
    arr = list(map(int, input().split()))
ans = 0

for i in range(n):
    if arr[i] == 0 and (i == 0 or (i > 0 and arr[i - 1] == 1)):
        ans += 1

print(ans)