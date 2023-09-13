#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        if(S>N*9 or (S==0 and N>1)): return '-1'
        num=""
        
        while(S>=9):
            num+="9" 
            N-=1
            S-=9
        
        while(N>0):
            if(S!=0):
                num+=str(S)
                S=0
            else: num+="0"
            N-=1

        return num

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends