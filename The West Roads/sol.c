#include <stdio.h>

int solve(int x) {
    return x * (x - 1) / 2;
}

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);
    printf("%d\n", solve(x));
    return 0;
}
