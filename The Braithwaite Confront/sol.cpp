#include <iostream>
using namespace std;

int max(int a, int b) {
    return (a >= b) ? a : b;
}

void solve() {
    int n, m, r, c;
    cin >> n >> m >> r >> c;
    cout << max(n - r, r - 1) + max(m - c, c - 1) << endl;
}

int main() {
    solve();
    return 0;
}
