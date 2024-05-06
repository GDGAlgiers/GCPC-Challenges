// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int &e: arr) cin >> e;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0 && (i == 0 || (i > 0 && arr[i - 1] == 1)))
        ans++;
    }
    cout << ans << '\n';
    

    return 0;
}