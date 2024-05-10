#include <stdio.h>

long solve(long x) {
    return x * (x - 1) / 2;
}

int main(int argc, char *argv[]) {
    long x;
    scanf("%ld", &x);
    printf("%ld\n", solve(x));
    return 0;
}
