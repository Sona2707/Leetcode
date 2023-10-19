#User function Template for python3

from collections import deque

class Solution:
    def nodeLevel(self, V, adj, X):
        q = deque()
        vis = [0] * V
        q.append((0, 0))
        vis[0] = 1
        while q:
            node, level = q.popleft()
            if node == X:
                return level
            for it in adj[node]:
                if not vis[it]:
                    q.append((it, level + 1))
                    vis[it] = 1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends