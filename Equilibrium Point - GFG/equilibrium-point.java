//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while (t-- > 0) {
            
            //taking input n
            int n = Integer.parseInt(br.readLine().trim());
            long arr[] = new long[n];
            String inputLine[] = br.readLine().trim().split(" ");
            
            //adding elements to the array
            for (int i = 0; i < n; i++) {
                arr[i] = Long.parseLong(inputLine[i]);
            }

            Solution ob = new Solution();
            
            //calling equilibriumPoint() function
            System.out.println(ob.equilibriumPoint(arr, n));
        }
    }
}
// } Driver Code Ends


class Solution {
    public int equilibriumPoint(long[] a, int n) {
        if (n == 1) {
            return 1; // Only one element is always an equilibrium point.
        }

        long totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += a[i];
        }

        long leftSum = 0;
        for (int i = 0; i < n; i++) {
            // Calculate rightSum by subtracting leftSum and the current element from totalSum.
            long rightSum = totalSum - leftSum - a[i];

            if (leftSum == rightSum) {
                return i + 1; // Return 1-based index of equilibrium point.
            }

            leftSum += a[i]; // Update leftSum for the next iteration.
        }

        return -1; // No equilibrium point found.
    }
}

