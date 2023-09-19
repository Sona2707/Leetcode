#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    def getFirstSetBit(self, n):
        pos = 1
        
        while n != 0:
            bit = n % 2
            
            if bit == 1:
                return pos
            pos += 1
            n //= 2  # Use floor division to get an integer result
        
        return 0

        

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends