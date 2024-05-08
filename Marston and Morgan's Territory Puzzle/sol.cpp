#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector< vector<ll> > graph;

ll n, m;
graph undirectedGraph;
vector< ll> isVisited, even, odd;
bool isValid = true;

void dfs(ll src, ll parent) {
	if (isVisited[parent] & 1) {
		isVisited[src] = 2;
		odd.push_back(src);
	}
	else {
		isVisited[src] = 1;
		even.push_back(src);
	}
	for (auto it: undirectedGraph[src]) {
		if (!isVisited[it]) {
			dfs(it, src);
		} else if ((isVisited[it] & 1) == isVisited[src] & 1) {
			isValid = false;
		}
	}
}

void solve() {
	cin >> n >> m;
	undirectedGraph.resize(n + 1);
	for (int i =0; i< m; ++i) {
		ll u, v;
		cin >> u >> v;
		undirectedGraph[u].push_back(v);
		undirectedGraph[v].push_back(u);
	}
	isVisited.resize(n+1);
	for (int i=1; i<=n; ++i) {
		if ((!isVisited[i]) && (undirectedGraph[i].size()))
			dfs(i, i);
	}
	if(!isValid) {
		return void(cout << -1);
	}
	cout << odd.size()<<'\n';
	for (auto it: odd) cout<<it<<' ';
	cout<<'\n';
	cout<<even.size()<<'\n';
	for (auto it:even) cout<<it<<' ';
}

signed main() {
	int tt = 1;
	while (tt--) {
		solve();
		cout<<endl;
	}
	return 0;
}