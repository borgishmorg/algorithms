#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

struct node{
	int status,
		parent,
		root,
		dist;
	vector<int> edges;
} g[101000];

int n, k, v;

int q[201000], l, r;

void bfs(int s){
	q[r++] = s;
	g[s].status = 1;
	g[s].root = s;
	g[s].parent = 0;
	while(l!=r){
		int pos = q[l];
		
		for(int i = 0; i < g[pos].edges.size(); i++){
			int next = g[pos].edges[i];
			if(!g[next].status){
				g[next].status = 1;
				g[next].root = s;
				g[next].dist = g[pos].dist + 1;
				g[next].parent = pos;
				q[r++] = next;
			}
		}
		l++;
	}
}

int bfs_forest(){
	int s = 0;
	for(int i = 1; i <= n; i++){
		g[i].root = 0;
		g[i].dist = 0;
		g[i].status = 0;
		g[i].parent = 0;
	}
	
	for(int i = 1; i <= n; i++){
		if(!g[i].status){
			bfs(i);
			s++;
		} 
	}
	
	return s;
}

void way(int pos){
	if(!g[pos].dist) return;
	way(g[pos].parent);
	cout << pos << ' ';
}

int main(){
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> n;
	for(int i = 1; i <= n; i++){
		cin >> k;
		for(int j = 1; j <= k; j++){
			cin >> v;
			g[i].edges.push_back(v);
		}
	}
	
	bfs(n);
	
	for(int i = 1; i < n; i++){
		cout << g[i].dist << " ";
		if(g[i].dist){
			way(i);
		}
		cout << '\n';
	}
	
	cout << bfs_forest();
	
	return 0;
}
/*
21
1 2
2 1 5
2 4 6
1 3
2 2 6
4 3 5 7 8
4 6 8 9 10
4 6 7 9 10
3 7 8 10
4 7 8 9 20
1 13
1 14
1 11
1 12
1 16
2 15 17
2 16 18
1 17
0
2 10 21
1 20
*/
