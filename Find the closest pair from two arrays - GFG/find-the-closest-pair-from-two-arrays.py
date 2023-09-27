#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        i,j=0,m-1
        diff=1e9
        val1,val2=-1,-1
        while(i<n and j>=0):
            sum=arr[i]+brr[j]
            
            if(abs(sum-x)<diff):
                diff=abs(sum-x)
                val1,val2=arr[i],brr[j]
                
            
            if(sum<=x):
                i+=1
            else:
                j-=1
        
        return [val1,val2]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends