def solve(x:int):
    sum = 0
    for x in range(1, x):
        sum += x
    return sum


x = int(input())
print(solve(x))