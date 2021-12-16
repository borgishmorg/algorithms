#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

struct nodes{
	int status;
	vector<int> edges;
} g[200000];

int n, u, v;

void dfs(int u){
	g[u].status = 1;
	for(int i = 0; i < g[u].edges.size(); i++){
		int v = g[u].edges[i];
		if(!g[v].status) dfs(v);
	}
}

int count(){
	int s = 0;
	for(int i = 1; i <= n; i++){
		if(g[i].status) continue;
		s++;
		dfs(i);
	}
	return s;
}

int main(){
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin >> n;
	while(cin >> u >> v){
		g[u].edges.push_back(v);
		g[v].edges.push_back(u);
	}
	cout << count();
	return 0;
}

