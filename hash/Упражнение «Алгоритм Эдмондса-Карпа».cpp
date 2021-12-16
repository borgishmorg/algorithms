#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int n;
int f[505][505], c[505][505];
int status[505], parent[505];

vector<int> adj[505];

int l, r;
int q[20200];

int bfs(){
	int path;
	for(int u = 1; u <= n; u++){
		status[u] = parent[u] = 0;
	}
	l = r = path = 0;
	q[r++] = 1;
	status[1] = 1;
	while(l < r && path == 0){
		int u = q[l];
		for(int i = 0; i < adj[u].size(); i++){
			int v = adj[u][i];
			if(status[v] == 0 && c[u][v] - f[u][v] > 0){
				status[v] = 1;
				parent[v] = u;
				if(v == n){
					path = 1;
					break;
				}
				q[r++] = v;
			}
		}
		l++;
	}
	return path;
}

int EDMONDS_KARP(){
	int F = 0;
	
	while(1){
		if(bfs() == 0)
			break;
		int gf = 1e9;
		int v = n;
		while(v != 1){
			int u = parent[v];
			gf = min(gf, c[u][v] - f[u][v]);
			v = u;
		}
		v = n;
		while(v != 1){
			int u = parent[v];
			f[u][v] += gf;
			f[v][u] = - f[u][v];
			v = u;
		}
		F = 0;
		for(int u = 1; u <= n; u++)
			F += f[1][u];
	}
	
	return F;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n;
	int ut, vt, ct;
	while(cin >> ut >> vt >> ct){
		c[ut][vt] = ct;
		adj[ut].push_back(vt);
		adj[vt].push_back(ut);
	} 
	cout << EDMONDS_KARP() << '\n';
	for(int u = 1; u <= n; u++){
		for(int v = 1; v <= n; v++){
			printf("%8d ", f[u][v]);
		}
		printf("\n");
	}
	return 0;
}

