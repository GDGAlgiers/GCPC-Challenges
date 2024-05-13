n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

cnt_a = 0
cnt_b = 0
stop = False

for i in range(1, k + 1):
    if i in a or i in b:
        if i in a:
            cnt_a += 1
        if i in b:
            cnt_b += 1
    else:
        stop = True
        break

if cnt_a >= k // 2 and cnt_b >= k // 2 and not stop:
    print('1')
else:
    print('0')
