//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    int n = sc.nextInt();
                    int sum = sc.nextInt();
                    int arr[] = new int[n];
                    for(int i = 0;i<n;i++)
                    arr[i] = sc.nextInt();
                    
                    Solution ob = new Solution();
                    System.out.println(ob.perfectSum(arr,n,sum));
                }
        }
}    
// } Driver Code Ends


class Solution {
    static int MOD = 1000000007;

    public int perfectSum(int arr[], int n, int sum) {
        int[][] dp = new int[n + 1][sum + 1];

        // Initialize dp[0][0] to 1 because there is one way to make a sum of 0
        dp[0][0] = 1;

        // Calculate the count of subsets that sum up to each possible value
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= sum; j++) {
                dp[i][j] = dp[i - 1][j];
                if (arr[i - 1] <= j) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - arr[i - 1]]) % MOD;
                }
            }
        }

        // The answer is stored in dp[n][sum]
        return dp[n][sum];
    }
}