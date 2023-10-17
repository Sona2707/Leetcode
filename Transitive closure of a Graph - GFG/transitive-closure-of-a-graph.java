//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int N = Integer.parseInt(in.readLine());
            int graph[][] = new int[N][N];
            
            for(int i = 0;i < N;i++)
                {String a[] = in.readLine().trim().split("\\s+");
                for(int j=0;j<N;j++)
                graph[i][j] = Integer.parseInt(a[j]);}
            
            Solution ob = new Solution();
            ArrayList<ArrayList<Integer>> ans = ob.transitiveClosure(N, graph);
            for(int i = 0;i < N;i++)
               { for(int j = 0;j < ans.get(i).size();j++)
                    System.out.print(ans.get(i).get(j) + " ");
            System.out.println();}
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static void setDfs(ArrayList<Integer>[] adj, int[] visited, int index) {
        visited[index] = 1;
        for (int x : adj[index]) {
            if (visited[x] != 1) {
                setDfs(adj, visited, x);
            }
        }
    }

    static ArrayList<ArrayList<Integer>> transitiveClosure(int N, int[][] graph) {
        ArrayList<Integer>[] adj = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            adj[i] = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                if (i != j && graph[i][j] == 1) {
                    adj[i].add(j);
                }
            }
        }

        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int[] visited = new int[N];
            visited[i] = 1;
            setDfs(adj, visited, i);
            ArrayList<Integer> visitedList = new ArrayList<>();
            for (int v : visited) {
                visitedList.add(v);
            }
            ans.add(visitedList);
        }

        return ans;
    }
}
