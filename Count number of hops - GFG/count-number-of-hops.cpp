//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    // Function to count the number of ways in which the frog can reach the top.
    long long countWays(int n) {
        const int MOD = 1000000007;
        
        // Create an array to store the number of ways for each step.
        // Initialize the first three steps manually as the frog can jump 1, 2, or 3 steps.
        long long ways[n + 1];
        ways[0] = 1; // Base case: There's one way to be at step 0.
        ways[1] = 1; // One way to be at step 1.
        ways[2] = 2; // Two ways to be at step 2 (1+1 or 2).

        // Calculate the number of ways for each step from 3 to n.
        for (int i = 3; i <= n; i++) {
            // The number of ways to reach step i is the sum of ways to reach
            // the previous three steps (i-1, i-2, and i-3).
            ways[i] = (ways[i - 1] + ways[i - 2] + ways[i - 3]) % MOD;
        }

        // Return the number of ways to reach the top (step n) modulo 1000000007.
        return ways[n];
    }
};


//{ Driver Code Starts.
int main()
{
    //taking testcases
	int t;
	cin >> t;
	
	while(t--)
	{
	    //taking number of steps in stair
		int n;
		cin>>n;
		Solution ob;
		//calling function countWays()
		cout << ob.countWays(n) << endl;
	}
    
    return 0;
    
}

// } Driver Code Ends