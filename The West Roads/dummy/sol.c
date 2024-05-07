#include <stdio.h>

long solve(long x) {
    long sum = 0;
    for (long i = 1; i < x; i++) {
        sum += i;
    }
    return sum;
}

int main(int argc, char *argv[]) {
    long x;
    scanf("%ld", &x);
    printf("%ld\n", solve(x));
    return 0;
}
