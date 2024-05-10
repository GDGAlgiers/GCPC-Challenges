#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int ca = 0, cb = 0;
    
    bool stop = false;
    for (int i = 1; i <= k; i++) {
        auto exists_a = binary_search(a.begin(), a.end(), i);
        auto exists_b = binary_search(b.begin(), b.end(), i);
        if (exists_a || exists_b) {
            if (exists_a) ca++;
            if (exists_b) cb++;
        } else {
            stop = true;
        }
    }
    if (ca >= k / 2 && cb >= k / 2 && !stop) cout << "1" << "\n";
    else cout << "0" << "\n";
        
 
    return 0;
}