class Solution:
    def duplicates(self, arr, n): 
    	
    	base=n
    	ans=[]
    	for i in range(n):
    	    num=arr[i]%base
    	    
    	    arr[num]=base+arr[num]; 
    	   
    	
    	for i in range(n):
            if(arr[i]//base>1): ans.append(i)
        

        return ans if len(ans)!=0 else [-1]

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends