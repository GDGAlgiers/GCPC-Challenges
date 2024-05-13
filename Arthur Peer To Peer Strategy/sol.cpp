#include <queue>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <iostream>


using namespace std;
const int infinity =  0x3f3f3f3f;

const int N = 1e5 + 5;


int e_num= 1, head[N], cur[N];
int v_num, s, t;
struct Node {
    int v;
    int next;
    int val;
} node[100 * N];

inline void add(int u, int v, int val) {
    node[++e_num].v = v;
    node[e_num].val = val;
    node[e_num].next = head[u];
    head[u] = e_num;
}


int dep[N], gap[N];
void bfs() {
    memset(dep, -1, sizeof(dep));
    memset(gap, 0, sizeof(gap));
    dep[t] = 0;
    gap[0] = 1;
    queue<int>q;
    q.push(t);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i=head[u]; i; i = node[i].next) {
            int v = node[i].v;
            if (dep[v] != -1 ) continue;
            q.push(v);
            dep[v] = dep[u] + 1;
            gap[dep[v]]++;
        }
    }

    return;
}

int maxflow;
int dfs(int u, int flow) {
    if (u == t) {
        maxflow += flow;
        return flow;
    }

    int used = 0;
    for (int i = cur[u]; i ; i= node[i].next) {
        int d = node[i].v;
        cur[u] = i;
        if (node[i].val && dep[d] + 1 == dep[u]) {
            int mi = dfs(d, min(node[i].val, flow-used));
            if (mi) {
                node[i].val -=mi;
                node[i^1].val +=mi;
                used +=mi;
            }
            if (used == flow) return used;
        } 
    }

    --gap[dep[u]];
    if (gap[dep[u]] == 0) dep[s] = v_num + 1;
    dep[u]++;
    gap[dep[u]]++;
    return used;
}

int ISAP() {
    maxflow = 0;
    bfs();
    while(dep[s] < v_num) {
        memcpy(cur, head, sizeof head); 
        dfs(s, infinity);
    }

    return maxflow;
}

void addedge(int u, int v, int f) {
    add(u, v, f);
    add(v, u, 0);
}

int n, m, u, v, w;
int num[N];
char c;
bool mp[55][55];

int main() {
    cin >> n>> m;
        memset(mp, 0, sizeof mp);
        v_num = 2*n;
        e_num = 1;
        memset(head, 0 , sizeof head); 
        for (int i= 1; i<=n; ++i) {
            num[i] = e_num + 1;
            addedge(i, i+n, 1);
        }

        for (int k=1; k<=m; k++) {
            cin >> c >> u >> c >> v >> c;
            ++u, ++v;
            addedge(u+n, v, infinity);
            addedge(v+n, u, infinity);
            mp[u][v] = mp[v][u] = 1;
        }

        int ans = infinity;
        for (int i=1; i<=n; ++i) {
            for (int j=i+1; j<=n; ++j) {
                if(!mp[i][j]) {
                    s = i +n;
                    t = j;
                    for (int l=1; l<=n; ++l) {
                        node[num[l]].val = 1;
                        node[num[l]^1].val = 0;
                    }
                    ans = min(ans, ISAP());
                }
            }
        }

        if (ans == infinity) cout << n << "\n";
        else cout << ans << "\n";
}