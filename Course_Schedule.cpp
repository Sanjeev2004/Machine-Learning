#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n);
    vector<int> indegree(n, 0);
    vector<int> topo;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--, b--; // 0 based indexing
        adj[a].push_back(b);
        indegree[b]++;
    }

    queue<int> q;
    for (int i = 0; i < n; i++)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
        }
    }
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        topo.push_back(node);
        for (auto it : adj[node])
        {
            indegree[it]--;
            if (indegree[it] == 0)
            {
                q.push(it);
            }
        }
    }

    if (topo.size() != n)
    {
        cout << "IMPOSSIBLE";
    }
    else
    {
        for (auto it : topo)
        {
            cout << it + 1 << " ";
        }
    }
    return 0;
}